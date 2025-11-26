# AI Customer Support Ticket Router

## 🔍 Overview

This project is an AI-powered customer support helper that:

- Classifies incoming customer messages into categories:
  - **Billing**, **Technical**, **Account**, or **Other**
- Assigns a priority level:
  - **Low**, **Medium**, or **High**
- Generates a short, friendly **support reply** for the customer

The goal is to show how a Solutions Engineer / AI Engineer can combine:
- LLMs (GPT)
- Simple Python backend
- Basic evaluation
to build a practical, business-focused solution.

---

## 🧠 How It Works

### 1. Route & Reply (`main.py`)

- Loads the OpenAI API key from `.env`
- Uses a system prompt to instruct the model to:
  - Read the user’s message
  - Decide `category` and `priority`
  - Generate a `reply`
- Returns a JSON-like response:

```json
{
  "category": "Billing",
  "priority": "High",
  "reply": "We're sorry to hear about the payment issue..."
}
