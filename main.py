import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def route_ticket(message: str) -> dict:
    """
    Takes a customer message and returns:
    - category: Billing / Technical / Account / Other
    - priority: Low / Medium / High
    - reply: AI-generated response to user
    """

    system_prompt = """
You are a customer support triage system for a tech service.

Your tasks are:
1. Read the user's message.
2. Decide the best category: "Billing", "Technical", "Account", or "Other".
3. Decide priority: "Low", "Medium", or "High".
4. Write a short, friendly reply to the user.

Respond ONLY in valid JSON with this structure:
{
  "category": "...",
  "priority": "...",
  "reply": "..."
}
Do not add extra text or explanation.
"""

    user_prompt = f"User message: {message}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # if this gives an error, we'll change this name
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content

    # Try to parse JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"raw_output": content}

    return data


if __name__ == "__main__":
    while True:
        user_message = input("\nEnter a customer message (or 'q' to quit): ")

        if user_message.lower() == "q":
            print("Exiting.")
            break

        result = route_ticket(user_message)

        print("\nModel output:")
        print(f"Category: {result.get('category')}")
        print(f"Priority: {result.get('priority')}")
        print(f"Reply: {result.get('reply') or result.get('raw_output')}")
