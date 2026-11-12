from neo4j import GraphDatabase
import os
from typing import List, Dict, Any

class GraphService:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "password")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query: str, parameters: Dict[str, Any] = None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]

    def add_entity(self, label: str, properties: Dict[str, Any]):
        """
        Adds a node to the graph.
        """
        query = f"MERGE (n:{label} {{id: $id}}) SET n += $props"
        # Ensure 'id' is in properties for MERGE to work uniquely
        if "id" not in properties:
            raise ValueError("Entity properties must contain an 'id' field.")
            
        self.execute_query(query, {"id": properties["id"], "props": properties})

    def add_relation(self, source_id: str, source_label: str, target_id: str, target_label: str, relation_type: str, properties: Dict[str, Any] = {}):
        """
        Adds a relationship between two nodes.
        """
        query = (
            f"MATCH (a:{source_label} {{id: $source_id}}), (b:{target_label} {{id: $target_id}}) "
            f"MERGE (a)-[r:{relation_type}]->(b) "
            f"SET r += $props"
        )
        self.execute_query(query, {
            "source_id": source_id, 
            "target_id": target_id, 
            "props": properties
        })

    def query_graph(self, cypher_query: str) -> List[Dict[str, Any]]:
        return self.execute_query(cypher_query)
