import os
from openai import OpenAI

# Configuración del servidor local vLLM corriendo en Docker
VLLM_URL = os.getenv("VLLM_URL", "http://localhost:8000/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Meta-Llama-3-8B-Instruct")

def get_vllm_client() -> OpenAI:
    """Devuelve un cliente OpenAI apuntando al motor vLLM local."""
    return OpenAI(
        base_url=VLLM_URL,
        api_key="token-no-requerido-para-vllm"
    )