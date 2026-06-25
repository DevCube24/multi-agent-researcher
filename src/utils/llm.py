import os
from openai import OpenAI
from typing import List, Dict, Optional

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str, model: str = "gpt-4o-mini", system_prompt: str = "You are a helpful assistant.") -> str:
    """Standard interface to call OpenAI models."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content
