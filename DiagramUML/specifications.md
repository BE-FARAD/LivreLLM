# Spécifications - Application Lecture Interactive de Livres Techniques

## Vue d'ensemble

Application permettant de :
1. Convertir des livres PDF techniques en Markdown
2. Stocker et indexer le contenu dans une base vectorielle (Qdrant)
3. Traduire les livres EN → FR
4. Lire les livres avec synthèse vocale (TTS)
5. Interagir avec un LLM pour poser des questions
6. Générer des fiches mémoire par chapitre

---

## Architecture - Packages et Classes

### 1. Package Input

#### Classe : FileWatcher

| Aspect | Description |
|--------|-------------|
| **Rôle** | Surveiller le répertoire `01-input` et détecter les nouveaux fichiers PDF |
| **Déclenchement** | À l'ouverture de l'application OU par clic utilisateur |
| **Identification** | Par nom de fichier ET hash (MD5/SHA256) du contenu |
| **Vérification** | Interroge Qdrant pour vérifier si le fichier existe déjà |
| **Limite** | Un fichier à la fois (contraintes de tokens) |

**Attributs :**
- `inputDirectory: String = "01-input"`
- `qdrantClient: QdrantClient`

**Méthodes :**
- `scanOnStartup()` : Scan au démarrage de l'application
- `scanOnUserClick()` : Scan déclenché par l'utilisateur
- `checkFileExists(file)` : Vérifie dans Qdrant si le fichier existe (hash)
- `computeHash(file)` : Calcule le hash du fichier
- `validatePDF(file)` : Valide que le fichier est un PDF valide

---

### 2. Package Conversion

#### Classe : MarkerConverter

| Aspect | Description |
|--------|-------------|
| **Rôle** | Convertir un PDF en Markdown via la bibliothèque [Marker](https://github.com/VikParuchuri/marker) |
| **Entrée** | Fichier PDF |
| **Sortie** | MarkdownDocument avec structure (chapitres, paragraphes) |
| **Extraction** | Images, tableaux, formules LaTeX |

**Attributs :**
- `markerConfig: MarkerConfig`

**Méthodes :**
- `convert(pdfFile)` : Conversion principale
- `extractImages(pdfFile)` : Extraction des images
- `extractTables(pdfFile)` : Extraction des tableaux
- `extractMathFormulas(pdfFile)` : Extraction des formules LaTeX
- `preserveStructure()` : Préservation de la structure chapitres/sections

---

#### Classe : MarkdownDocument

| Aspect | Description |
|--------|-------------|
| **Rôle** | Représenter un document Markdown structuré |
| **Structure** | Contient des chapitres, qui contiennent des paragraphes |
| **Métadonnées** | Langue, nom du livre, auteur, etc. |

**Attributs :**
- `content: String`
- `language: String` (détecté automatiquement)
- `bookName: String`
- `chapters: List<Chapter>`
- `metadata: Metadata`

---

#### Classe : Chapter

| Aspect | Description |
|--------|-------------|
| **Rôle** | Représenter un chapitre du livre |
| **Contenu** | Paragraphes, images associées, formules mathématiques, code de programmation|

**Attributs :**
- `number: int`
- `title: String`
- `content: String`
- `sections: List<Section>`
- `images: List<Image>`
- `formulas: List<LaTeXFormula>`

---

#### Classe : Paragraph

| Aspect | Description |
|--------|-------------|
| **Rôle** | Représenter un paragraphe avec ses médias associés |
| **Association** | Images et formules mathématique, code liées au contexte du paragraphe |

**Attributs :**
- `number: int`
- `content: String`
- `associatedImages: List<Image>` (lien contextuel)
- `associatedFormulas: List<LaTeXFormula>`

---

### 3. Package Storage

#### Classe : ImageManager

| Aspect | Description |
|--------|-------------|
| **Rôle** | Gérer le stockage et le nommage des images |
| **Structure** | `images/{nomLivre}/` |
| **Nommage** | `{nomLivre}_ch{XX}_img{XXX}.png` |
| **Unicité** | Garantie par le format de nommage |

**Exemple de structure :**
```
images/
└── clean_code/
    ├── clean_code_ch01_img001.png
    ├── clean_code_ch01_img002.png
    ├── clean_code_ch02_img001.png
    └── ...
```

---

#### Classe : AudioManager

| Aspect | Description |
|--------|-------------|
| **Rôle** | Gérer la génération et le stockage des fichiers audio |
| **Structure** | `audio/{nomLivre}/` |
| **Nommage** | `{nomLivre}_ch{XX}_para{XXX}.mp3` |
| **Génération** | Une seule fois par paragraphe (coût TTS) |
| **Récupération** | Télécharge l'audio existant si déjà généré |

**Exemple de structure :**
```
audio/
└── clean_code/
    ├── clean_code_ch01_para001.mp3
    ├── clean_code_ch01_para002.mp3
    └── ...
```

---

#### Classe : TTSService

| Aspect | Description |
|--------|-------------|
| **Rôle** | Service de synthèse vocale (Text-to-Speech) |
| **Langue** | Français par défaut |
| **API** | À définir (OpenAI TTS, ElevenLabs, etc.) |

**Questions ouvertes :**
- [ ] Quelle API TTS utiliser ?
- [ ] Comment traiter les formules mathématiques à l'oral ?
- [ ] Comment traiter les blocs de code à l'oral ?

---

### 4. Package Vectorization

#### Classe : QdrantClient

| Aspect | Description |
|--------|-------------|
| **Rôle** | Client pour la base vectorielle Qdrant |
| **Stockage** | Vecteurs + métadonnées des livres |
| **Vérification** | Permet de vérifier si un livre existe déjà (hash) |

---

#### Classe : VectorStore

| Aspect | Description |
|--------|-------------|
| **Rôle** | Abstraction pour l'indexation et la recherche |
| **Indexation** | Par document ou par chapitre |
| **Recherche** | Retourne les chunks les plus pertinents |

---

#### Classe : TextChunker

| Aspect | Description |
|--------|-------------|
| **Rôle** | Découper le texte en chunks pour l'indexation |
| **Stratégie** | Par chapitre ou par paragraphe |
| **Contexte** | Préservation du contexte entre chunks |

**Questions ouvertes :**
- [ ] Taille des chunks ?
- [ ] Overlap entre chunks ?

---

#### Classe : EmbeddingService

| Aspect | Description |
|--------|-------------|
| **Rôle** | Générer les embeddings pour les chunks |
| **Modèle** | À définir |

**Questions ouvertes :**
- [ ] Quel modèle d'embedding ?

---

### 5. Package Translation

#### Classe : TranslationService

| Aspect | Description |
|--------|-------------|
| **Rôle** | Traduire les documents EN → FR |
| **Moteur** | Utilise le LLMClient |
| **Préservation** | Code, formules LaTeX, références images |
| **Déclenchement** | Après conversion si document en anglais |

---

#### Classe : DocumentManager

| Aspect | Description |
|--------|-------------|
| **Rôle** | Gérer la sauvegarde et le chargement des documents |
| **Structure** | `02-output/{nomLivre}/{lang}/{nomLivre}.md` |
| **Versions** | Stocke les deux versions (EN + FR) |

**Exemple de structure :**
```
02-output/
└── clean_code/
    ├── en/
    │   └── clean_code.md
    └── fr/
        └── clean_code.md
```

---

### 6. Package LLM

#### Classe : LLMClient

| Aspect | Description |
|--------|-------------|
| **Rôle** | Client unique pour toutes les interactions LLM |
| **Utilisations** | Traduction, résumé, Q&A, génération fiches |
| **Langue** | Échanges en français |

---

#### Classe : RAGEngine

| Aspect | Description |
|--------|-------------|
| **Rôle** | Moteur RAG pour les questions contextuelles |
| **Fonctionnement** | Récupère contexte depuis VectorStore + interroge LLM |

---

### 7. Package ReadingSession

#### Classe : ReadingSessionManager

| Aspect | Description |
|--------|-------------|
| **Rôle** | Gérer une session de lecture interactive |
| **Flux** | Sélection chapitre → Résumé → Lecture → Q&A → Fiche |
| **Audio** | Lance la lecture audio paragraphe par paragraphe |
| **Interruption** | L'utilisateur peut interrompre pour poser des questions |

**Flux de lecture :**
1. Utilisateur sélectionne un chapitre (liste déroulante)
2. LLM génère un résumé introductif
3. LLM commence la lecture (avec audio)
4. Utilisateur peut interrompre pour poser des questions
5. LLM répond puis reprend la lecture
6. Fin du chapitre → génération de la fiche mémoire

---

#### Classe : MemoryCardGenerator

| Aspect | Description |
|--------|-------------|
| **Rôle** | Générer une fiche mémoire à la fin d'un chapitre |
| **Contenu** | Résumé, points clés, formules, Q&A |
| **Format** | Markdown |
| **Stockage** | Associée au chapitre |

---

#### Classe : MemoryCard

| Aspect | Description |
|--------|-------------|
| **Rôle** | Représenter une fiche mémoire |
| **Contenu** | Voir ci-dessous |
| **Format** | Markdown |

**Contenu de la fiche :**
- Résumé du chapitre
- Points clés / concepts importants
- Formules importantes (LaTeX)
- Questions posées par l'utilisateur
- Réponses du LLM
- Date de création

---

### 8. Package UserSession

#### Classe : User

| Aspect | Description |
|--------|-------------|
| **Rôle** | Représenter un utilisateur |
| **Identification** | ID unique |
| **Préférences** | Langue, audio activé, voix préférée |

---

#### Classe : SessionPersistence

| Aspect | Description |
|--------|-------------|
| **Rôle** | Persister et restaurer les sessions de lecture |
| **Reprise** | Permet de reprendre là où l'utilisateur s'est arrêté |
| **Historique** | Sauvegarde l'historique de conversation |

---

#### Classe : ReadingState

| Aspect | Description |
|--------|-------------|
| **Rôle** | État d'une session de lecture |
| **Données** | Livre, chapitre, paragraphe, position audio, historique |

**Données persistées :**
- `userId`
- `bookName`
- `currentChapter`
- `currentParagraph`
- `audioPosition`
- `conversationHistory`
- `lastUpdated`

---

### 9. Package Orchestration

#### Classe : Pipeline

| Aspect | Description |
|--------|-------------|
| **Rôle** | Orchestrer le flux de traitement d'un nouveau livre |
| **Flux** | FileWatcher → Marker → Images → Traduction → Vectorisation → Audio |

---

#### Classe : ApplicationController

| Aspect | Description |
|--------|-------------|
| **Rôle** | Contrôleur principal de l'application (Streamlit) |
| **Actions** | Login, sélection livre/chapitre, lecture, Q&A |

---

## Questions ouvertes

### Audio (TTS)
- [ ] Quelle API TTS utiliser ? (OpenAI TTS, ElevenLabs, Google, Azure, local)
- [ ] Quelle voix française ?
- [ ] Comment traiter les formules mathématiques à l'oral ?
- [ ] Comment traiter les blocs de code à l'oral ?

### Vectorisation
- [ ] Taille des chunks ?
- [ ] Overlap entre chunks ?
- [ ] Quel modèle d'embedding ?

### Authentification
- [ ] Simple identifiant local ou OAuth ?

---

## Technologies utilisées

| Composant | Technologie |
|-----------|-------------|
| Interface | Streamlit |
| Conversion PDF | Marker |
| Base vectorielle | Qdrant |
| LLM | À définir |
| TTS | À définir |
| Embeddings | À définir |

---

## Structure des répertoires

```
project/
├── 01-input/                    # Dépôt des PDF
├── 02-output/                   # Documents Markdown
│   └── {bookName}/
│       ├── en/
│       │   └── {bookName}.md
│       └── fr/
│           └── {bookName}.md
├── images/                      # Images extraites
│   └── {bookName}/
│       └── {bookName}_ch{XX}_img{XXX}.png
├── audio/                       # Fichiers audio TTS
│   └── {bookName}/
│       └── {bookName}_ch{XX}_para{XXX}.mp3
├── memory_cards/                # Fiches mémoire
│   └── {bookName}/
│       └── {bookName}_ch{XX}_memory.md
└── sessions/                    # Sessions utilisateur
    └── {userId}/
        └── {bookName}_session.json
```
