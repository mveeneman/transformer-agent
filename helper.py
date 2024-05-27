# Add your utilities or helper functions to this file.

import os

def get_openai_api_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_huggingface_api_key():
    huggingface_api_key = os.getenv("HUGGING_FACE_HUB_TOKEN")
    return huggingface_api_key