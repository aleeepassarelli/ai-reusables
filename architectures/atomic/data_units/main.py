import json

with open("atoms/data_units/context_medical.jsonl") as f:
    docs = [json.loads(line) for line in f]

rag.ingest(docs)
