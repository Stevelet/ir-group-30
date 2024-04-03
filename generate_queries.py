from transformers import T5Tokenizer, DataCollatorForSeq2Seq
from transformers import T5ForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer

MODEL_NAME = "google/flan-t5-xl"

tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

batch = tokenizer(
    "The capital of Canada is",
    return_tensors="pt",
    add_special_tokens=False
)

batch = {k: v.to("cpu") for k, v in batch.items()}
generated = model.generate(batch["input_ids"], max_length=100)
print(tokenizer.decode(generated[0]))