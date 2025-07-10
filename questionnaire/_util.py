import requests, json, os

from ._prompts_website_generation import PROMPT, SYSTEM_PROMPT

from google import genai

URL = "http://localhost:11434/api/chat"

client_google = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))


def gemini(prompt: str):
    response = client_google.models.generate_content(
        model="gemini-2.0-flash",
        config=genai.types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT),
        contents=prompt
    )
    
    return response.text.replace('`', '').replace('python', '')


def llama_check_answers(prompt: str):
    data = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": prompt

            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, json=data)

    return response.json()["message"]["content"]


def llama_website_content(system_prompt: str, prompt: str):
    data = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt

            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, json=data)

    return response.json()["message"]["content"]


def anthropic_answers(prompt: str):
    messages = [{
        "role": "user",
        "content": prompt
    }]

    """ message = client_anthropic.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=1024,
        messages=messages,
        system=PROMPT
    )

    return message.content """


def anthropic_website_content(prompt: str):
    messages = [{
        "role": "user",
        "content": prompt
    }]
    
    """ message = client_anthropic.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=8192,
        messages=messages,
        system=SYSTEM_PROMPT
    )

    return message.content """


def open_router(system_prompt: str, prompt: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "anthropic/claude-sonnet-4",
            "messages": [
            {
                "role": "user",
                "content": prompt
            }
            ],
            "system": system_prompt,
            "max_tokens": 2096
        }),
    )

    print(response.content.decode('utf-8'))

    return response.content.decode('utf-8')




def draft_knowledge(qandas) -> str:
    relevant_info = ''

    for qa in qandas:
        question = qa.question
        answer = qa.answer

        if not answer:
            continue

        relevant_info += f'\n\n<question>{question}</question>\n<answer>{answer}</answer>\n' 

    return relevant_info