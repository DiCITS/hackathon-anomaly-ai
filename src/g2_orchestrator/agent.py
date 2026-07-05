from typing import List, Dict, Any
from src.config import get_vllm_client, MODEL_NAME

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
        # TODO: Diseñar un System Prompt estricto y forzar formato JSON (Structured Outputs)
        
        # El retorno esperado por el sistema debe seguir esta estructura exacta:
        return {
            "tipo_anomalia": "Ej: Variación súbita de frecuencia",
            "algoritmo_recomendado": "Ej: IsolationForest",
            "justificacion_cientifica": "Ej: Basado en el paper X, debido a alta dimensionalidad...",
            "parametros_sugeridos": {"n_estimators": 100, "contamination": 0.05}
        }