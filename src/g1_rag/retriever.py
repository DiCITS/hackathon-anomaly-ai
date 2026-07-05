from typing import List

class KnowledgeRetriever:
    def __init__(self, papers_dir: str = "data/papers"):
        self.papers_dir = papers_dir
        # TODO: Inicializar aquí la base de datos vectorial (Chroma/FAISS) 
        # y el modelo de embeddings local si fuera necesario.
        pass

    def ingest_papers(self) -> None:
        """Lee los PDFs de data/papers, los trocea y los indexa."""
        # TODO: Implementar lógica de carga y chunking
        pass

    def get_relevant_context(self, user_query: str, top_k: int = 3) -> List[str]:
        """
        Dado un problema del usuario, busca los fragmentos más relevantes en los papers.
        
        CONTRATO DE ENTRADA: user_query (str)
        CONTRATO DE SALIDA: List[str] (Fragmentos de texto científico literal)
        """
        # TODO: Implementar búsqueda por similitud cuántica/coseno
        return ["Contexto dummy 1", "Contexto dummy 2"]