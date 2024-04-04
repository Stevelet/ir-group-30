import transformers
from dotenv import load_dotenv

load_dotenv()

device = "cpu"

import os

k_drive = os.path.join(os.getcwd(), "..", "..", "..", "mnt", "k")
cache_path = os.path.join(k_drive, "cache")
trec_data = os.path.join(k_drive, "trec")
terrier_path = os.path.join(k_drive, "terrier")


# tokenizer = transformers.LlamaTokenizer.from_pretrained("huggyllama/llama-7b", cache_dir=cache_path)
# model = transformers.LlamaForCausalLM.from_pretrained("huggyllama/llama-7b", load_in_4bit=True, cache_dir=cache_path)

import pyterrier as pt
from pathlib import Path

if not pt.started():
    pt.init(tqdm="notebook", home_dir=terrier_path)

dataset = pt.get_dataset('irds:trec-fair/2022')

iter = dataset.get_corpus_iter()

for item in iter:
    pass

# batch = tokenizer(
#     "The capital of Canada is",
#     return_tensors="pt",
#     add_special_tokens=False
# )
# batch = {k: v.to("cpu") for k, v in batch.items()}
# generated = model.generate(batch["input_ids"], max_length=30)
# print(tokenizer.decode(generated[0]))
