from typing import Dict, Any
from src.config import get_vllm_client, MODEL_NAME

class CodeGenerator:
    def __init__(self):
        self.client = get_vllm_client()

    def generate_python_script(self, strategy_dict: Dict[str, Any]) -> str:
        """
        Recibe el diccionario de estrategia de G2 y genera un script ejecutable de Python.
        
        CONTRATO DE ENTRADA: strategy_dict (Dict)
        CONTRATO DE SALIDA: str (Código Python puro, listo para pasar por exec() o guardar)
        """
        # TODO: Diseñar prompt para evitar que el LLM devuelva markdown (```python ... ```)
        # o texto conversacional. Debe devolver código puro e independiente.
        
        return "import pandas as pd\nprint('Script autogenerado en blanco')"