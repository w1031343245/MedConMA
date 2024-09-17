from openai import OpenAI
import httpx


client = OpenAI(
    base_url="", 
    api_key="",
    http_client=httpx.Client(
        base_url="",
        follow_redirects=True,
    ),
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content

def chat_with_gpt2(systen_role, prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        temperature=0,
        max_tokens=50,
        messages=[
            {"role": "system", "content": systen_role},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content
