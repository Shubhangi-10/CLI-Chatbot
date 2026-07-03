import os
import sys
try:
    from google import genai
except Exception:
    genai = None

API_KEY = os.environ.get("GEMINI API KEY")

MODEL_NAME = "gemini-2.0-flash" 


def get_api_key():
    key = API_KEY
    if not key:
        key = input("Enter your Gemini API key: ").strip()
    if not key:
        print("No API key provided. Exiting.")
        sys.exit(1)
    return key


def main():
    api_key = get_api_key()

    try:
        client = genai.Client(api_key=api_key)
        chat = client.chats.create(model=MODEL_NAME)
    except Exception as e:
        print(f"Error initializing model: {e}")
        sys.exit(1)

    print("=" * 50)
    print(" Gemini Chatbot (type 'exit' or 'quit' to stop)")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}")
        except Exception as e:
            print(f"\n[Error] Could not get a response: {e}")


if __name__ == "__main__":
    main()
