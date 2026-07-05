# 🚀 AnomalyAI: Copiloto Autónomo de Data Science

Bienvenido al repositorio base de **AnomalyAI**, el MVP de nuestra startup. 

Este proyecto implementa una arquitectura multi-agente diseñada para resolver un cuello de botella industrial crítico: el tiempo que transcurre desde que ocurre una anomalía en una planta hasta que el equipo de I+D lee la literatura, diseña una estrategia y despliega el código para detectarla. Nuestro sistema automatiza este proceso de semanas a segundos utilizando Modelos de Lenguaje de Gran Escala (LLMs) desplegados localmente.

---

## 🏗️ Arquitectura del Sistema

El sistema está compuesto por cuatro microservicios (agentes), cada uno asignado a un equipo de desarrollo:

1. **`g1_rag/` (Motor de Ingesta Científica):** Lee PDFs académicos y extrae conocimiento empírico sobre detección de anomalías utilizando bases de datos vectoriales.
2. **`g2_orchestrator/` (Motor de Lógica):** Analiza el problema, procesa los papers y decide mediante *Prompt Engineering* estricto qué algoritmo matemático aplicar (salida en JSON).
3. **`g3_programmer/` (Motor de Generación):** Toma la estrategia de G2 y genera autónomamente código Python puro (`pandas`, `scikit-learn`) listo para producción.
4. **`g4_evaluator/` (Motor de Auditoría):** Agente de QA que cruza toda la información anterior y emite un veredicto de calidad científica y técnica antes de aprobar el código.

---

## ⚙️ Prerrequisitos

* **Sistema Operativo:** Linux/Ubuntu
* **Hardware:** GPU NVIDIA con soporte CUDA (Mínimo 16GB VRAM para modelos 8B).
* **Software:** * `python` >= 3.10
  * `docker` y `nvidia-container-toolkit` instalados.

---

## 🚀 Despliegue Rápido (Setup)

### 1. Levantar el Motor de Inferencia (vLLM)
Todo el sistema consume la API de un modelo local . Levanta el servidor en una terminal independiente:

```bash
docker run --gpus all \
  --name vllm-server \
  -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --ipc=host \
  vllm/vllm-openai:latest \
  --model meta-llama/Meta-Llama-3-8B-Instruct \
  --gpu-memory-utilization 0.90 \
  --max-model-len 4096