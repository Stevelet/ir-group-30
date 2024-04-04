# Prompts based on https://arxiv.org/abs/2310.13243

PROMPT_DICT = {
    "msmarco-v1-passage": {
        "huggyllama/llama-7b": "Generate a question that is the most relevant to the given passage."
                               "\nPassage: {doc}\n\nHere is a generated relevant question: ",
    },
    "beir-v1.0.0-trec-covid.flat": {
        "huggyllama/llama-7b": "Generate a question that is the most relevant to the given article."
                               "\n{doc}\n\nHere is a generated relevant question: ",
    }
}
