# Book Reader - Contexte Projet

> Application de Lecture Interactive de Livres Techniques

---

## RÈGLES OBLIGATOIRES

### 1. RESPECT STRICT DU PLAN

- **TOUJOURS** consulter `docs/specifications/structure-projet.md` avant de coder
- **TOUJOURS** suivre l'ordre de développement des 6 phases
- **JAMAIS** sauter une étape ou une classe
- **JAMAIS** implémenter une classe sans avoir terminé ses dépendances

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6
   ↓         ↓         ↓         ↓         ↓         ↓
 TESTS    TESTS     TESTS     TESTS     TESTS     TESTS
```

### 2. VALIDATION OBLIGATOIRE AVANT PASSAGE À LA SUITE

Pour chaque classe implémentée :

```
[ ] 1. Code conforme au diagramme UML
[ ] 2. Tests unitaires écrits et passants (pytest)
[ ] 3. Tests d'intégration si dépendances
[ ] 4. Documentation des méthodes (docstrings)
[ ] 5. Revue du code par l'utilisateur
[ ] 6. VALIDATION EXPLICITE de l'utilisateur avant de continuer
```

**⚠️ NE JAMAIS passer à la classe suivante sans validation explicite.**

### 3. WORKFLOW DE DÉVELOPPEMENT PAR CLASSE

```
1. LIRE    → docs/specifications/specifications.md
2. LIRE    → docs/architecture/uml/pdf-converter-classes.puml
3. CRÉER   → Fichier Python selon structure-projet.md
4. CODER   → Implémenter la classe
5. TESTER  → Écrire tests unitaires (tests/test_{classe}.py)
6. EXÉCUTER → pytest tests/test_{classe}.py
7. CORRIGER → Si échec, corriger jusqu'à 100% pass
8. VALIDER → Demander validation utilisateur
9. ATTENDRE → Confirmation avant de continuer
```

---

## STRUCTURE DU PROJET

```
book-reader/
│
├── CLAUDE.md                           # CE FICHIER - Règles du projet
├── README.md                           # Documentation principale
│
├── docs/                               # 📚 DOCUMENTATION
│   ├── specifications/                 # Spécifications fonctionnelles
│   │   ├── specifications.md           # Description des classes
│   │   ├── structure-projet.md         # Structure et ordre de dev
│   │   └── decisions-techniques.md     # Choix technologiques
│   │
│   └── architecture/                   # Architecture technique
│       ├── uml/                        # Diagrammes de classes
│       │   ├── pdf-converter-classes.puml
│       │   └── pdf-converter.puml
│       │
│       └── sequences/                  # Diagrammes de séquence
│           ├── sequence-01-import.puml
│           └── sequence-02-lecture.puml
│
├── .claude/                            # 🤖 CONFIGURATION CLAUDE
│   ├── commands/                       # Commandes slash
│   │   ├── implement-class.md          # /implement-class {Classe}
│   │   ├── validate-class.md           # /validate-class {Classe}
│   │   ├── run-tests.md                # /run-tests {module}
│   │   ├── status.md                   # /status
│   │   └── next.md                     # /next
│   └── agents/                         # Sous-agents
│
├── PRPs/                               # 📋 Product Requirements Prompts
│
├── src/                                # 💻 CODE SOURCE
│   ├── input/                          # Package Input
│   ├── conversion/                     # Package Conversion
│   ├── storage/                        # Package Storage
│   ├── vectorization/                  # Package Vectorization
│   ├── translation/                    # Package Translation
│   ├── llm/                            # Package LLM
│   ├── reading/                        # Package ReadingSession
│   ├── user/                           # Package UserSession
│   └── orchestration/                  # Package Orchestration
│
├── app/                                # 🖥️ INTERFACE STREAMLIT
│   ├── pages/
│   └── components/
│
├── tests/                              # 🧪 TESTS (OBLIGATOIRE)
│
├── data/                               # 📁 DONNÉES
│   ├── 01-input/
│   ├── 02-output/
│   ├── images/
│   ├── audio/
│   ├── memory_cards/
│   └── sessions/
│
└── config/                             # ⚙️ CONFIGURATION
```

---

## COMMANDES SLASH DISPONIBLES

| Commande | Description |
|----------|-------------|
| `/implement-class {Classe}` | Implémenter une classe avec tests |
| `/validate-class {Classe}` | Valider une classe avant passage |
| `/run-tests {module}` | Exécuter les tests |
| `/status` | Voir l'avancement du projet |
| `/next` | Voir la prochaine classe à implémenter |

---

## FICHIERS DE RÉFÉRENCE

| Fichier | Chemin | Contenu |
|---------|--------|---------|
| Spécifications | `docs/specifications/specifications.md` | Description des classes |
| Structure | `docs/specifications/structure-projet.md` | Ordre de développement |
| Décisions | `docs/specifications/decisions-techniques.md` | Choix techniques |
| UML Classes | `docs/architecture/uml/pdf-converter-classes.puml` | Diagramme de classes |
| UML Activité | `docs/architecture/uml/pdf-converter.puml` | Diagramme d'activité |
| Séquence Import | `docs/architecture/sequences/sequence-01-import.puml` | Flux d'import |
| Séquence Lecture | `docs/architecture/sequences/sequence-02-lecture.puml` | Flux de lecture |

---

## STACK TECHNIQUE

| Composant | Technologie |
|-----------|-------------|
| Python | 3.12 |
| Gestionnaire | uv |
| LLM | OpenAI GPT-4o mini + Ollama |
| TTS | OpenAI Realtime |
| Embeddings | text-embedding-3-small/large |
| Vector DB | Qdrant (Docker) |
| Interface | Streamlit |
| Tests | pytest |
| Linter | ruff |

---

## CHECKLIST PAR PHASE

### Phase 1 : Infrastructure
- [ ] config/ et .env
- [ ] FileWatcher - Tests ✓ - Validé ✓
- [ ] MarkerConverter - Tests ✓ - Validé ✓
- [ ] MarkdownDocument - Tests ✓ - Validé ✓
- [ ] Chapter - Tests ✓ - Validé ✓
- [ ] Paragraph - Tests ✓ - Validé ✓
- [ ] ImageManager - Tests ✓ - Validé ✓
- [ ] DocumentManager - Tests ✓ - Validé ✓

### Phase 2 : Vectorisation et LLM
- [ ] QdrantClient - Tests ✓ - Validé ✓
- [ ] EmbeddingService - Tests ✓ - Validé ✓
- [ ] TextChunker - Tests ✓ - Validé ✓
- [ ] VectorStore - Tests ✓ - Validé ✓
- [ ] LLMClient - Tests ✓ - Validé ✓
- [ ] TranslationService - Tests ✓ - Validé ✓

### Phase 3 : Audio et Distillation
- [ ] TTSService - Tests ✓ - Validé ✓
- [ ] DistillationService - Tests ✓ - Validé ✓
- [ ] AudioManager - Tests ✓ - Validé ✓

### Phase 4 : Session de lecture
- [ ] User - Tests ✓ - Validé ✓
- [ ] UserPreferences - Tests ✓ - Validé ✓
- [ ] AppSettings - Tests ✓ - Validé ✓
- [ ] SessionPersistence - Tests ✓ - Validé ✓
- [ ] ReadingState - Tests ✓ - Validé ✓
- [ ] RAGEngine - Tests ✓ - Validé ✓
- [ ] ReadingSessionManager - Tests ✓ - Validé ✓
- [ ] MemoryCard - Tests ✓ - Validé ✓
- [ ] MemoryCardGenerator - Tests ✓ - Validé ✓

### Phase 5 : Interface Streamlit
- [ ] Page Settings - Tests ✓ - Validé ✓
- [ ] Page Import - Tests ✓ - Validé ✓
- [ ] Page Library - Tests ✓ - Validé ✓
- [ ] Page Reader - Tests ✓ - Validé ✓
- [ ] Composants UI - Tests ✓ - Validé ✓

### Phase 6 : Orchestration
- [ ] Pipeline - Tests ✓ - Validé ✓
- [ ] ApplicationController - Tests ✓ - Validé ✓
- [ ] Tests d'intégration globaux ✓

---

## RAPPEL FINAL

```
⚠️  AVANT CHAQUE NOUVELLE CLASSE :
    1. Vérifier que la précédente est VALIDÉE
    2. Vérifier que les TESTS passent
    3. Obtenir CONFIRMATION de l'utilisateur

🚫 INTERDIT :
    - Sauter des étapes
    - Implémenter sans tests
    - Passer à la suite sans validation
```
