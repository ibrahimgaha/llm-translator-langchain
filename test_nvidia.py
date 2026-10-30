
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise ValueError("NVIDIA_API_KEY missing from .env")

url = "https://integrate.api.nvidia.com/v1/chat/completions"

payload = {
    "model": "nvidia/riva-translate-4b-instruct-v2",
    "messages": [
        {
            "role": "system",
            "content": "en-fr"
        },
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "temperature": 0,
    "max_tokens": 256
}

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=60
)

print("HTTP Status:", response.status_code)

if response.ok:
    result = response.json()
    print("Translation:",
          result["choices"][0]["message"]["content"])
else:
    print("API Error:", response.text[:1000])
