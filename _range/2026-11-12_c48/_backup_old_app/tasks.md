# Tâches de Reprise du Programme (Conformité Méthodologie Hybride)

## 1. Configuration de l'Environnement
- [ ] Installer les nouvelles dépendances : `pip install -r requirements.txt`
- [ ] Installer Marker (si nécessaire via script externe ou s'assurer que `marker-pdf` fonctionne).
- [ ] Configurer le fichier `.env` avec les clés suivantes :
    - `OPENAI_API_KEY`
    - `ANTHROPIC_API_KEY` (pour Claude / Contextual Retrieval)
    - `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD` (pour le Graphe)
    - `QDRANT_URL`, `QDRANT_API_KEY` (si utilisation de Qdrant Cloud, sinon local par défaut)

## 2. Validation de l'Ingestion (ETL)
- [ ] Tester l'upload d'un PDF via l'endpoint `/ingest/upload`.
- [ ] Vérifier que la conversion Marker génère bien un Markdown dans `processed_data/{book_id}/`.
- [ ] Vérifier que les chunks sont bien créés et enrichis par Claude (Contextualization).
- [ ] Vérifier que les vecteurs sont bien insérés dans Qdrant.
- [ ] Vérifier que les entités/relations sont bien extraites et insérées dans Neo4j.

## 3. Amélioration de la Recherche (Hybrid Search)
- [ ] Affiner le prompt d'extraction de Graphe dans `llm_service.py` (actuellement générique).
- [ ] Implémenter une stratégie de recherche de graphe plus poussée dans `chat.py` (ex: Cypher Query Generation).
- [ ] Tester la qualité des réponses combinées (Vecteur + Graphe).

## 4. Frontend (Si applicable)
- [ ] Mettre à jour le frontend pour utiliser l'endpoint `/ingest/upload` au lieu de `/books/upload`.
- [ ] Adapter l'affichage pour supporter le streaming de réponse ou l'affichage des sources (Graphe vs Texte).

## 5. Évolution LivreLLM (Actuel)
- [ ] **Extraction & Parsing**
    - [x] Améliorer la détection des chapitres (Regex/Heuristique) <!-- id: 0 -->
    - [x] Intégrer `marker-pdf` ou similaire pour une meilleure structure <!-- id: 1 -->
- [ ] **RAG Avancé**
    - [ ] Implémenter la recherche hybride (Qdrant) <!-- id: 2 -->
    - [ ] Ajouter le filtrage par métadonnées <!-- id: 3 -->
- [ ] **UI/UX**
    - [ ] Ajouter les couvertures de livres <!-- id: 4 -->
    - [ ] Barre de progression de lecture <!-- id: 5 -->