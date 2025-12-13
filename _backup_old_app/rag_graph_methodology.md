# Méthodologie RAG Hybride : Vectoriel (Qdrant) & Graphe (Neo4j)

Ce document détaille l'approche technique utilisée pour la **Couche Connaissance** d'HyperRAG, combinant la puissance de la recherche sémantique (Vectorielle) et la précision structurelle (Graphe).

---

## 1. Architecture Vectorielle (Qdrant)
**Objectif** : Retrouver des passages de texte pertinents par similarité sémantique (le "Sens").

### Étape 1 : Ingestion & Préparation (ETL)
1.  **Source** : Fichiers PDF bruts (DTP, Normes) dans `01_INPUTS`.
2.  **Conversion** : Utilisation de `Docling` / `Marker` pour convertir le PDF en **Markdown enrichi**.
    *   *Avantage* : Conserve la structure (Titres, Tableaux) et les références d'images.
3.  **Chunking (Découpage)** :
    *   Découpage du Markdown en segments logiques (par section ou par taille de fenêtre).
    *   Préservation du contexte (Overlap) pour ne pas couper des phrases.

### Étape 2 : Indexation (Embeddings)
1.  **Modèle** : OpenAI `text-embedding-3-small`.
2.  **Processus** : Chaque chunk de texte est transformé en un vecteur mathématique (liste de nombres).
3.  **Stockage** : Les vecteurs sont stockés dans **Qdrant** (Base de données vectorielle).
    *   Organisation : Une **Collection** par Tome (ex: `hyperrag_tome_1`).
    *   Métadonnées : Chaque vecteur garde le lien vers le fichier source et la page.

### Étape 3 : Recherche (Retrieval)
1.  **Query** : La question de l'utilisateur est convertie en vecteur.
2.  **Search** : Qdrant compare ce vecteur avec ceux de la base (Cosine Similarity).
3.  **Result** : Retourne les 5 à 10 passages les plus proches sémantiquement.

---

## 2. Architecture Graphe de Connaissance (Neo4j)
**Objectif** : Comprendre et naviguer dans les relations complexes entre les objets (la "Structure").

### Étape 1 : Modélisation (Ontologie)
Nous définissons les types d'entités et de relations pertinents pour un Poste HTB :
*   **Noeuds (Nodes)** : `Equipement` (Disjoncteur), `Fonction` (Protection), `Lieu` (Travée), `Document` (Norme).
*   **Relations (Edges)** : `EST_CONNECTÉ_À`, `ALIMENTE`, `RÉGULE_PAR`, `DÉCRIT_DANS`.

### Étape 2 : Extraction (LLM)
1.  **Analyse** : Un LLM (GPT-4) lit les chunks de texte.
2.  **Extraction** : Il identifie les entités et leurs relations.
    *   *Exemple* : "Le Disjoncteur D1 est relié au Sectionneur S1" ➔ `(D1)-[:EST_RELIÉ_À]->(S1)`.
3.  **Peuplement** : Génération de requêtes **Cypher** pour insérer ces données dans **Neo4j**.

### Étape 3 : Interrogation (Graph RAG)
1.  **Query** : "Quels sont tous les équipements connectés au jeu de barres ?"
2.  **Traversal** : Neo4j parcourt le graphe de proche en proche.
3.  **Result** : Retourne une liste exhaustive d'équipements, même s'ils ne sont pas cités dans le même paragraphe (impossible pour le vectoriel seul).

---

## 3. Optimisation : Contextual Retrieval (Approche Claude)
**Objectif** : Résoudre le problème des "chunks orphelins" (morceaux de texte qui perdent leur sens une fois coupés du document).

### Le Problème
Un chunk classique : *"La valeur doit être de 50m."*
➔ **Problème** : De quelle valeur parle-t-on ? De quel équipement ? L'embedding sera flou.

### La Solution (Contextualisation)
Avant d'indexer, nous utilisons **Claude (Anthropic)** pour générer un contexte explicite pour chaque chunk.

1.  **Prompt** : "Voici le document complet. Voici un extrait. Explique le contexte de cet extrait en une phrase."
2.  **Génération** : Claude génère : *"Ce passage définit la distance de garde minimale pour un disjoncteur 225kV selon la norme C13-100."*
3.  **Fusion** :
    *   **Chunk Stocké** : *"La valeur doit être de 50m."* (Texte original).
    *   **Chunk Indexé** : *"Ce passage définit la distance de garde... La valeur doit être de 50m."* (Texte enrichi).

### Résultat
L'embedding capture maintenant le **sens complet**. La recherche retrouve ce passage même si la question ne contient pas les mots exacts du chunk original, mais parle du concept général.

---

## 4. Synthèse : L'Approche Hybride (Triangulaire)
Le système HyperRAG interroge les deux moteurs en parallèle pour construire sa réponse :

| Moteur | Force | Usage Typique |
| :--- | :--- | :--- |
| **Qdrant** | Recherche floue, concepts, explications textuelles. | "Comment fonctionne la protection différentielle ?" |
| **Neo4j** | Relations exactes, hiérarchie, dépendances physiques. | "Liste les composants de la travée départ." |

**Résultat** : Une réponse riche (texte) et précise (structure).
