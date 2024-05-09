from django.conf import settings
import openai


if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY
else:
    raise Exception('OpenAI API Key not found')


def get_completion(prompt, context):
    messages = [{"role": "user", "content": prompt}]
    for item in context:
        messages.append({"role": "system", "content": item.question})
        messages.append({"role": "user", "content": item.answer})

    query = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    response = query.get('choices')[0]['message']['content']
    return response
