import openai
from django.conf import settings

def generate_message(message):
    api_key = settings.OPEN_AI_KEY
    print(api_key)
    openai.api_key = str(api_key)
    completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=message
)

    msg =completion.choices[0].message.content

    return msg
