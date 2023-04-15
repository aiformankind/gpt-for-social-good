import dotenv
import openai
import os

dotenv.load_dotenv('../.env')
openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": "tell me about gpt for social good"}
    ]
)

print(response["choices"][0]["message"]["content"])