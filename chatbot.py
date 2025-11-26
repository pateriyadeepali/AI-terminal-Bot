import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found in .env file")
    exit()

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash",
    system_instruction=(
        "Answer in maximum 10 lines, simple plain text only. "
        "No bold, no lists, no headings. "
        "Give clear and short explanations."
    )
)

print("\nGemini Terminal Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Bye!")
        break

    try:
        response = model.generate_content(
            user_input,
            generation_config={
                "response_mime_type": "text/plain"
            }
        )
        print("Bot:", response.text)
    except Exception as e:
        print("Error:", e)
