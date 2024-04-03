# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
#
# model_name = "huggyllama/llama-7b"
#
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     load_in_4bit=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_compute_dtype=torch.bfloat16,
#     device_map="cpu"
# )
# tokenizer = AutoTokenizer.from_pretrained(
#     model_name,
#     trust_remote_code=True,
#     device_map="cpu"
# )
#
# batch = tokenizer(
#     "The capital of Canada is",
#     return_tensors="pt",
#     add_special_tokens=False
# )
#
# print("Reached")
#
# batch = {k: v.to("cpu") for k, v in batch.items()}
# generated = model.generate(batch["input_ids"], max_length=100)
# print(tokenizer.decode(generated[0]))

import transformers
from dotenv import load_dotenv

load_dotenv()

device = "cpu"

tokenizer = transformers.LlamaTokenizer.from_pretrained("huggyllama/llama-7b")
model = transformers.LlamaForCausalLM.from_pretrained("huggyllama/llama-7b", load_in_4bit=True)

batch = tokenizer(
    "The capital of Canada is",
    return_tensors="pt",
    add_special_tokens=False
)
