# Plan d'Implémentation : Évolution de LivreLLM

## Description de l'Objectif
L'objectif est de faire évoluer le prototype actuel "LivreLLM" vers un assistant vocal local robuste et de qualité professionnelle pour la lecture de livres. L'accent est mis sur l'amélioration de la qualité de l'extraction de contenu (PDF), l'intelligence de la recherche (RAG) et l'expérience utilisateur (UI/UX).

## Revue Utilisateur Requise
> [!IMPORTANT]
> **Changements de Dépendances** : Le passage à une analyse PDF robuste pourrait nécessiter l'installation de dépendances système (comme `ocr-my-pdf` ou `tesseract`) ou de paquets Python plus lourds (`marker-pdf`, `unstructured`).
> **Coûts API** : Le RAG amélioré et la "Traduction Intelligente" augmentent l'utilisation de tokens avec OpenAI.

## Risques et Considérations (À Valider)
1.  **Latence de Traduction** : Traduire un chapitre à la volée (Markdown + Structure) avec GPT-4o peut prendre 30-60s.
    *   *Mitigation* : Traduction en arrière-plan ou mise en cache agressive.
2.  **Coût du Contextual Retrieval** : Générer un contexte pour chaque chunk multiplie les appels API.
    *   *Mitigation* : Limiter aux résumés de chapitres ou activer uniquement sur demande.
3.  **Cohérence Audio** : L'audio est généré sur le texte traduit. Si la traduction change, l'audio doit être régénéré.

### 1. Ingestion & Traitement Robuste
L'architecture doit être **Modulaire** pour garantir la stabilité. Fini le code monolithique dans `app.py`.

#### [CRÉÉ] `core/` (Architecture Modulaire)
- **`core/scanner.py`** : Module isolé responsable de l'exécution de `marker-pdf`.
    - Gère les appels système (`subprocess`).
    - Gère les erreurs de dépendances Python (Numpy/Torch).
    - Retourne un chemin de fichier Markdown validé ou lève une erreur explicite.
- **`core/splitter.py`** (À venir) : Module responsable du découpage intelligent en chapitres.

#### [MODIFIER] `app.py` (Interface UI uniquement)
- Ne contient **AUCUNE** logique métier complexe.
- Appelle simplement `core.scanner.scan_pdf_with_marker()`.
- Affiche les barres de progression et les erreurs formatées par les modules `core`.

### 2. RAG Avancé (Contextual Retrieval & Multimodal)
(Reste inchangé pour l'instant)

...

## Flux de Travail (Workflow Standardisé)
1.  **Import** : Dépose PDF dans `01_INPUTS/`.
2.  **Scan Automatisé** (Via `core/scanner.py`) :
    *   Vérification de l'environnement (Marker installé ?).
    *   Exécution isolée de la commande `marker_single`.
    *   Validation de la sortie (fichier .md existant).
3.  **Traitement** (Via `core/splitter.py` & `core/translator.py`) :
    *   Découpage en chapitres.
    *   Traduction LLM.
    *   Stockage structuré.
3.  **Indexation (RAG)** :
    *   Génération de contexte pour chaque chunk (Contextual Retrieval).
    *   Indexation dans Qdrant (Texte + Contexte).
4.  **Lecture** :
    *   L'utilisateur ouvre un livre.
    *   Affichage du livre traduit avec images.
5.  **Audio** :
    *   L'utilisateur clique sur "Lire".
    *   LLM donne un résumé du chapitre. 
    *   l'utilisateur clique sur lecture du résumé ou la lecture du livre.
    *   Génération de l'audio (si absent) avec mapping paragraphes <-> timestamps.
    *   Lecture synchronisée.
    *   l'enregistrement de la lecture est stocké dans `library_data/{book_id}/audio.
    *  la sauvegarde du résumé et des echanges avec l'utilisateur sont stockées dans `library_data/{book_id}/chat_history.json`.    
    *  l'utilisateur peut consulter les echanges avec l'utilisateur dans la vue "Chat".
    *  l'utilisateur clique sur le chapitre suivant ou précédent pour lire le livre.       

## Plan de Vérification

### Tests Automatisés
- **Tests Unitaires** : Tester les fonctions de découpage de texte et de stockage des métadonnées.
- **Tests d'Intégration** : Vérifier le flux d'insertion et de récupération Qdrant.

### Vérification Manuelle
- **Upload PDF** : Tester avec un PDF complexe (images, colonnes) pour vérifier la qualité de l'extraction.
- **Précision RAG** : Poser des questions spécifiques sur le contenu du livre et vérifier la réponse par rapport au texte.
- **Flux Audio** : Vérifier que la "Lecture Intelligente" saute les blocs de code comme prévu.
