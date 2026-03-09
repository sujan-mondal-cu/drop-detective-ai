from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_community.llms import HuggingFacePipeline


def load_llm():

    model_id = "google/flan-t5-base"

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=200,   # allow longer answers
        temperature=0.3,
        do_sample=True
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm