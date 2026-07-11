import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Groq_api_key"))


def get_ai_explanation(algorithm: str, input_arr: list, steps: list) -> str:
    total_steps = len(steps)

    first_step  = steps[0]                 if steps else None
    middle_step = steps[total_steps // 2]  if steps else None
    last_step   = steps[-1]                 if steps else None

    prompt = f"""
Algorithm: {algorithm}
Input array: {input_arr}
Total steps taken: {total_steps}

Representative steps from the trace:
  First:  {first_step}
  Middle: {middle_step}
  Last:   {last_step}

Explain in plain English:
1. Why did this specific run take exactly {total_steps} steps?
2. Where was the most expensive part of this run?
3. What does the Big-O mean for an input of size {len(input_arr)}, using the actual numbers above?

Do NOT just say "O(n²) is slow". Tie your answer to the actual step count from this trace.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.4,
    )

    return response.choices[0].message.content.strip()