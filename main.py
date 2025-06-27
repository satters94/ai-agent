import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
inputs = sys.argv


def main():
    if len(inputs) > 1: 
        user_prompt = inputs[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
        response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
        )
        print(f"Text response: {response.text}")
        if len(inputs) > 2 and inputs[2] == "--verbose":
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        error_message = "No prompt provided!"
        print(error_message)
        sys.exit(1)


if __name__ == "__main__":
    main()
