# État Actuel de l'Application LivreLLM

## 🚨 RÈGLES CRITIQUES INVIOLABLES
1. **Conversion PDF** : TOUJOURS utiliser `marker-pdf` (commande `marker_single`). JAMAIS de `LlamaParse`, `PyMuPDF` ou autre.
2. **Format Fichier** : TOUJOURS travailler avec du **Markdown (.md)**, jamais de `.txt`.
3. **Architecture** : Respecter le plan : Scan -> `marker` -> Markdown -> Découpage Chapitres -> Traduction.
4. **Pas de Modification Sauvage** : Ne jamais supprimer une fonctionnalité existante sans demande explicite.

## 📅 Dernière Mise à Jour : 05 Décembre 2025

## 🚀 Avancement Global
L'application est en cours de transformation vers une architecture **"Local-First & High-Fidelity"**.
- **Interface** : Style "Apple Books" (Fait).
- **Extraction** : Passage de `pypdf` à `marker-pdf` pour une haute fidélité (Maths, Code, Images) (Fait).
- **Workflow** : Redéfinition complète du flux (Scan -> Traduction -> Stockage -> Lecture).

## 🛠 Architecture Technique Validée

### 1. Ingestion & Traitement (ETL)
- **Moteur** : `marker-pdf` (avec fallback sur `pymupdf4llm`).
- **Processus** :
    1.  Conversion PDF -> Markdown (Images extraites).
    2.  Découpage en Chapitres (Titres Markdown).
    3.  **Traduction Immédiate** : Traduction du Markdown en Français dès le scan.
    4.  **Stockage** : Conservation des deux versions (`chapter_X_en.md` et `chapter_X_fr.md`) dans `library_data/{book_id}/`.

### 2. RAG Avancé (Contextual Retrieval)
- **Stratégie** : Contextual Retrieval + Multimodal.
- **Indexation** :
    - Chaque chunk est enrichi par un contexte généré par LLM.
    - Indexation dans Qdrant (Local).
- **Images** : Liées au texte et affichables.

### 3. Expérience de Lecture & Audio
- **Lecture** : Affichage par défaut de la version Française traduite.
- **Flux Audio** :
    1.  Clic sur "Lecture".
    2.  **Résumé Vocal** : Génération d'un résumé du chapitre par LLM.
    3.  **Choix Utilisateur** : Écouter le résumé OU le chapitre entier.
    4.  **Génération** : TTS (OpenAI) avec synchronisation (Mapping Paragraphe <-> Timestamp).
    5.  **Stockage** : `library_data/{book_id}/audio/`.
- **Chat** :
    - Historique sauvegardé dans `library_data/{book_id}/chat_history.json`.
    - Consultation possible via une vue dédiée.

## 📝 Tâches en Cours (Basé sur implementation_plan.md)
- [x] Intégration `marker-pdf`.
- [ ] Implémentation de la Traduction au Scan (Backend).
- [ ] Implémentation du Contextual Retrieval (RAG).
- [ ] Mise en place du Workflow Audio (Résumé vs Lecture complète).
- [ ] Sauvegarde de l'historique de Chat.

## 📂 Structure des Fichiers Clés
- `app.py` : Point d'entrée (Streamlit).
- `library_data/` :
    - `{book_id}/`
        - `images/` : Images extraites.
        - `audio/` : Fichiers MP3.
        - `chapter_X_fr.md` : Texte traduit.
        - `chat_history.json` : Historique des conversations.
