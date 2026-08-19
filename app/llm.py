import os
from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "")
client = OpenAI()

def ask(instructions, prompt):
    if not MODEL:
        raise RuntimeError("Set OPENAI_MODEL to a model available in your account.")
    response = client.responses.create(model=MODEL, instructions=instructions, input=prompt)
    return response.output_text.strip()
