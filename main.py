import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
inputs = sys.argv

def main():
    if len(inputs) > 1: 
        response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=inputs[1]
        )
        print(f"Text response: {response.text}")

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        error_message = "No prompt provided!"
        print(error_message)
        sys.exit(1)


if __name__ == "__main__":
    main()
