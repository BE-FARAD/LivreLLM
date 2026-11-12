from openai import OpenAI
from anthropic import Anthropic
import os
from typing import List, Dict, Any
import json

class LLMService:
    def __init__(self):
        self.grok_api_key = os.getenv("GROK_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if self.grok_api_key:
            self.openai_client = OpenAI(
                api_key=self.grok_api_key,
                base_url="https://api.x.ai/v1"
            )
            self.model = os.getenv("LLM_MODEL", "grok-beta")
        else:
            self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = "gpt-4o"
            
        if self.anthropic_api_key and not self.anthropic_api_key.startswith("sk-ant-..."):
            self.anthropic_client = Anthropic(api_key=self.anthropic_api_key)
        else:
            self.anthropic_client = None

    def summarize_chapter(self, text: str) -> str:
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes book chapters in French."},
                {"role": "user", "content": f"Summarize the following text in French:\n\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def translate_text(self, text: str, target_lang: str = "French") -> str:
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"You are a professional translator. Translate the following text to {target_lang}. Return ONLY the translation."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    def answer_question(self, question: str, context: List[str]) -> str:
        context_str = "\n\n".join(context)
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an intelligent book assistant. Answer the user's question based on the provided context. Answer in French."},
                {"role": "user", "content": f"Context:\n{context_str}\n\nQuestion: {question}"}
            ]
        )
        return response.choices[0].message.content

    def contextualize_chunk(self, chunk: str, full_document_context: str) -> str:
        """
        Uses Claude (or fallback to main LLM) to generate a context string for a specific chunk.
        """
        prompt = f"""
        <document>
        {full_document_context[:10000]}... (truncated for brevity if too long)
        </document>
        
        <chunk>
        {chunk}
        </chunk>
        
        Please give a short context to situate this chunk within the overall document for the purpose of improving search retrieval. 
        Answer with just the context sentence(s).
        """
        
        if self.anthropic_client:
            message = self.anthropic_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        else:
            # Fallback to main LLM (Grok/OpenAI)
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides context for text chunks."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

    def extract_graph_entities(self, text: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Extracts entities and relationships for the Knowledge Graph.
        Returns a JSON object with 'nodes' and 'edges'.
        """
        prompt = f"""
        Analyze the following text and extract entities (nodes) and relationships (edges) for a knowledge graph.
        Focus on technical equipment, functions, locations, and documents.
        
        Text:
        {text}
        
        Return ONLY a JSON object with the following structure:
        {{
            "nodes": [
                {{"id": "unique_id", "label": "Type", "properties": {{...}}}}
            ],
            "edges": [
                {{"source": "source_id", "target": "target_id", "type": "RELATION_TYPE", "properties": {{...}}}}
            ]
        }}
        """
        
        # Check if model supports JSON mode (Grok might not yet, so we omit response_format if using Grok)
        kwargs = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert at extracting knowledge graphs from technical documentation. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ]
        }
        
        if "gpt" in self.model:
             kwargs["response_format"] = {"type": "json_object"}
        
        response = self.openai_client.chat.completions.create(**kwargs)
        
        content = response.choices[0].message.content
        # Strip markdown code blocks if present
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
            
        return json.loads(content.strip())
