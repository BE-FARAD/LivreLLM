from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.vector_service import VectorService
from backend.services.graph_service import GraphService
from backend.services.llm_service import LLMService

router = APIRouter(prefix="/chat", tags=["chat"])
vector_service = VectorService()
graph_service = GraphService()
llm_service = LLMService()

class ChatRequest(BaseModel):
    question: str
    book_id: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # 1. Vector Search (Semantic)
        vector_results = vector_service.search(f"book_{request.book_id}", request.question, limit=5)
        vector_context = [res["text"] for res in vector_results]
        
        # 2. Graph Search (Structural/Relational)
        # For a simple start, we can extract entities from the question and find their neighbors.
        # This is a basic implementation of Graph RAG.
        # TODO: Improve by using an LLM to generate a Cypher query or more complex traversal.
        
        # Placeholder for Graph Context
        graph_context = []
        # entities = llm_service.extract_entities(request.question) # We would need a simpler entity extractor
        # for entity in entities:
        #     neighbors = graph_service.query_graph(f"MATCH (n {{name: '{entity}'}})-[r]-(m) RETURN m.name, type(r), n.name")
        #     graph_context.extend([f"{row['n.name']} {row['type(r)']} {row['m.name']}" for row in neighbors])
        
        # Combine contexts
        full_context = vector_context + graph_context
        
        # 3. Generate Answer
        answer = llm_service.answer_question(request.question, full_context)
        
        return ChatResponse(
            answer=answer,
            sources=full_context
        )
    except Exception as e:
        print(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))
