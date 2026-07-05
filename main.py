import json
from src.g1_rag.retriever import KnowledgeRetriever
from src.g2_orchestrator.agent import StrategyOrchestrator
from src.g3_programmer.generator import CodeGenerator
from src.g4_evaluator.validator import SolutionEvaluator

def run_pipeline(user_problem: str):
    print("🚀 Iniciando Pipeline de AnomalyAI...")
    
    # Instanciar módulos
    retriever = KnowledgeRetriever()
    orchestrator = StrategyOrchestrator()
    programmer = CodeGenerator()
    evaluator = SolutionEvaluator()
    
    # 1. Ejecutar RAG
    print("\n[Paso 1] Buscando literatura científica...")
    contexts = retriever.get_relevant_context(user_problem)
    
    # 2. Ejecutar Orquestación
    print("[Paso 2] Diseñando estrategia técnica con LLM...")
    strategy = orchestrator.determine_strategy(user_problem, contexts)
    print(f"-> Estrategia: {strategy.get('algoritmo_recomendado')}")
    
    # 3. Generar Código
    print("[Paso 3] Programando solución autónoma...")
    code = programmer.generate_python_script(strategy)
    
    # 4. Evaluar Coherencia Cruzada
    print("[Paso 4] Iniciando auditoría y alineación científica...")
    report = evaluator.evaluate_pipeline(user_problem, contexts, strategy, code)
    
    # Resultado Final
    print("\n================ REPORT CARD FINAL ================")
    print(json.dumps(report, indent=4, ensure_ascii=False))
    print("====================================================")

if __name__ == "__main__":
    # Caso de prueba inicial para simular el pitch ante inversores
    FALLO_FABRICA = (
        "El sensor de temperatura de la turbina hidráulica presenta picos extraños "
        "cada 4 horas, pero la media general se mantiene estable. Queremos detectarlo."
    )
    run_pipeline(FALLO_FABRICA)