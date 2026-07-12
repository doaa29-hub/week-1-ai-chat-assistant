import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"

messages = [
    {"role": "system", "content": "You are a helpful, friendly assistant."}
]


def get_response(user_input: str) -> str:
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply


def main():
    print("=" * 50)
    print("AI Chat Assistant (type 'exit' or 'quit' to leave)")
    print("=" * 50)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            reply = get_response(user_input)
            print(f"Assistant: {reply}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
