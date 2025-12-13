# 📚 LivreLLM - Application Web

## 🎯 Fonctionnalités

✅ **Lecteur audio unique** - Un seul lecteur pour tout le chapitre (pas par paragraphe)
✅ **Chat intégré** - Posez des questions sur le chapitre en cours
✅ **Interface web moderne** - Design dark avec animations
✅ **Traduction automatique** - Les livres en anglais sont traduits en français
✅ **Audio en français** - Lecture audio en français via OpenAI TTS

## 🚀 Lancement

### Streamlit (Administration)
```bash
streamlit run app/main.py
```
Port: http://localhost:8501

**Utilisation**: 
- Import de livres PDF
- Conversion Markdown
- Gestion de la bibliothèque

### Flask (Lecture Web)
```bash
python web_app/app.py
```
Port: http://localhost:5001

**Utilisation**:
- Bibliothèque de livres
- Lecteur avec audio unique
- Chat avec IA

## 📖 Utilisation

### 1. Bibliothèque
- Page d'accueil: Liste tous les livres disponibles
- Cliquez sur "Lire →" pour ouvrir un livre

### 2. Lecteur
- **Sidebar gauche**:
  - Liste des chapitres (cliquez pour naviguer)
  - Section chat (posez des questions)
  
- **Zone principale**:
  - Bouton "▶ Lire le chapitre" (lecture audio complète)
  - Lecteur audio HTML5 (contrôles: play/pause, volume, timeline)
  - Contenu du chapitre

### 3. Chat
- Tapez votre question dans le champ
- Cliquez "Envoyer" ou appuyez sur Entrée
- L'IA répond en se basant sur le chapitre actuel

## 🎨 Design

- **Dark mode** professionnel
- **Gradients** modernes
- **Animations** fluides au survol
- **Responsive** (adapté mobile/desktop)

## 🔧 Architecture

```
web_app/
├── app.py              # Serveur Flask + API REST
├── templates/
│   ├── library.html    # Page bibliothèque
│   └── reader.html     # Page lecteur
└── static/
    ├── css/
    │   ├── library.css # Styles bibliothèque
    │   └── reader.css  # Styles lecteur
    └── js/
        └── reader.js   # Logique JavaScript
```

## 📡 API Endpoints

- `GET /` - Page bibliothèque
- `GET /reader/<book_name>` - Page lecteur
- `GET /api/book/<book_name>/chapters` - Liste des chapitres
- `GET /api/book/<book_name>/chapter/<num>` - Contenu d'un chapitre
- `POST /api/audio/<book_name>/chapter/<num>` - Génération audio
- `GET /audio/<book_name>/chapter/<num>/file` - Fichier audio
- `POST /api/chat` - Envoi question chat
- `GET /images/<book_name>/<image_name>` - Images du livre

## 🎧 Audio

- **Un seul lecteur** par chapitre
- **Cache intelligent** - Les fichiers audio sont mis en cache avec hash du contenu
- **Format**: MP3 via OpenAI TTS
- **Voix**: Définie dans `.env` (TTS_VOICE)

## 💬 Chat IA

- **Contexte**: Utilise le contenu du chapitre actuel
- **Modèle**: OpenAI GPT (défini dans `.env`)
- **Réponses**: En temps réel

## ⚙️ Configuration

Fichier `.env`:
```env
OPENAI_API_KEY=your_key_here
LLM_MODEL=gpt-4o-mini
TTS_VOICE=alloy
TTS_PROVIDER=openai
```

## 📝 Notes

- Les livres doivent être importés via l'interface Streamlit
- Les traductions sont mises en cache en session
- Les fichiers audio sont persistés dans `data/audio/`

## 🐛 Dépannage

**Port 5000 occupé par AirPlay?**
→ L'app utilise le port 5001

**Pas de livres affichés?**
→ Importez des PDF via Streamlit d'abord

**Audio ne se génère pas?**
→ Vérifiez votre clé API OpenAI dans `.env`
