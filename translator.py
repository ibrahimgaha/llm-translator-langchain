
import os
import requests

from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda

load_dotenv()

MODEL_NAME = "nvidia/riva-translate-4b-instruct-v2"

SUPPORTED_LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Arabic": "ar",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh",
    "Japanese": "ja",
}


def validate_translation_input(
    text: str,
    source_language: str,
    target_language: str,
):
    if not text or not text.strip():
        raise ValueError("Please enter some text to translate.")

    if source_language not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported source language.")

    if target_language not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported target language.")

    if source_language == target_language:
        raise ValueError("Choose two different languages.")


def call_nvidia_api(data: dict) -> str:
    """Send a translation request to NVIDIA Riva."""

    api_key = os.getenv("NVIDIA_API_KEY")

    if not api_key:
        raise ValueError("NVIDIA_API_KEY is missing.")

    source_code = SUPPORTED_LANGUAGES[data["source_language"]]
    target_code = SUPPORTED_LANGUAGES[data["target_language"]]

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": f"{source_code}-{target_code}",
            },
            {
                "role": "user",
                "content": data["text"],
            },
        ],
        "temperature": 0,
        "max_tokens": 1024,
    }

    response = requests.post(
        "https://integrate.api.nvidia.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"]


# LangChain workflow
translation_chain = RunnableLambda(call_nvidia_api)


def translate_text(
    text: str,
    source_language: str,
    target_language: str,
) -> str:
    """Validate the input and execute the LangChain workflow."""

    validate_translation_input(
        text,
        source_language,
        target_language,
    )

    result = translation_chain.invoke(
        {
            "text": text.strip(),
            "source_language": source_language,
            "target_language": target_language,
        }
    )

    return result.strip()
