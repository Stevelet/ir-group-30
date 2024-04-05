import transformers
from dotenv import load_dotenv
from pathlib import Path
import json
from prompts import PROMPT_DICT

load_dotenv()

device = "cpu"

import os

k_drive = os.path.join(os.getcwd(), "..", "..", "..", "mnt", "k")
cache_path = os.path.join(k_drive, "cache")
trec_data = os.path.join(k_drive, "trec")
terrier_path = os.path.join(k_drive, "terrier")
index_path = os.path.join(k_drive, "index")

augmented_index_path = os.path.join(index_path, "augmented_index.json")
generated_queries_path = os.path.join(index_path, "generated_queries.json")

tokenizer = transformers.LlamaTokenizer.from_pretrained("huggyllama/llama-7b", cache_dir=cache_path)
model = transformers.LlamaForCausalLM.from_pretrained("huggyllama/llama-7b", load_in_4bit=True, cache_dir=cache_path)

counter = 1
with open(augmented_index_path,'r',buffering=10000) as f:
    for line in f:
        di = json.loads(line)

        queries = []
        errored = False
        for prompt in PROMPT_DICT.values():
            if errored is True:
                continue
            for sub_prompt in prompt.values():
                token_prompt = sub_prompt.replace('{doc}', di['plain'])
                try:
                    batch = tokenizer(
                        token_prompt,
                        return_tensors="pt",
                        add_special_tokens=False
                    )
                    batch = {k: v.to("cuda") for k, v in batch.items()}
                    generated = tokenizer.decode(model.generate(batch["input_ids"], max_length=1024)[0])
                    queries.append(list(filter(lambda x: len(x) > 0, generated.replace(token_prompt, '').split('\n\n')))[0])
                except ValueError as e:
                    errored = True
        if not errored:
            counter += 1
            with open(generated_queries_path, 'a') as f1:
                f1.write(json.dumps({'id': di['id'], 'queries': queries}) + '\n')
            print(counter)
