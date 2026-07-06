from typing import List, Dict, Any
from src.config import get_vllm_client, MODEL_NAME
# from prompts import get_main_prompt

class StrategyOrchestrator:
    def __init__(self):
        self.client = get_vllm_client()

    def determine_strategy(self, user_problem: str, scientific_contexts: List[str]) -> Dict[str, Any]:
        """
        Analiza el problema del usuario cruzándolo con el contexto científico de G1
        y decide la mejor estrategia algorítmica.
        
        CONTRATO DE ENTRADA: user_problem (str), scientific_contexts (List[str])
        CONTRATO DE SALIDA: Dict (JSON estructurado obligatorio con claves específicas)
        """

        client = get_vllm_client()

        print("connection stablished with vLLM")

        ruta_archivo = "moc_rag.txt" # Reemplaza con la ruta de tu archivo
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            paper_content = archivo.read()
        
        response = client.chat.completions.create(
            model="google/gemma-4-31B-it",
            messages=[
                {"role": "system", "content": "Eres un agente inteligente"},
                {"role": "user", "content": get_main_prompt(paper_content)}
            ],
            temperature=0.7,
            response_format={"type": "json_object"},
            stream=True # streaming en tiempo real|
        )

        # Imprime la respuesta token por token
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)

        # TODO: Diseñar un System Prompt estricto y forzar formato JSON (Structured Outputs)
            
        # El retorno esperado por el sistema debe seguir esta estructura exacta:
        return {
            "tipo_anomalia": "Ej: Variación súbita de frecuencia",
            "algoritmo_recomendado": "Ej: IsolationForest",
            "justificacion_cientifica": "Ej: Basado en el paper X, debido a alta dimensionalidad...",
            "parametros_sugeridos": {"n_estimators": 100, "contamination": 0.05}
        }
    

def get_main_prompt(domain_context: str) -> str:
    """
    Devuelve el prompt principal para la orquestación de estrategias.
    Este prompt se utiliza para guiar al LLM en la toma de decisiones algorítmicas.
    """

    desired_structure = {
        "tipo_anomalia": "string",
        "algoritmo_recomendado": {
            "funcion": "Nombre_del_algoritmo",
            "parametros": ["a", "b"],
            "bloque": [
                {
                "instruccion": "asignar",
                "variable": "resultado",
                "valor": "a + b"
                },
                {
                "instruccion": "retornar",
                "valor": "resultado"
                }
            ]   
        },
        "justificacion_cientifica": "string",
        "parametros_sugeridos": "string"
    }

    prompt = f'''
    Con base en el contexto proporcionado a continuación:

    {domain_context}
    
    Vas a generar un algoritmo de alto nivel (sin una sitáxis específica de lenguaje de programación) que resuelva el problema.
    Vas a entregar la respuesta en un formato JSON estricto con la siguiente estructura:

    {desired_structure}
'''

    # print(prompt)
    return prompt