# 📚 Guide d'utilisation - Livres Français avec Audio

## ✅ Livres disponibles

### 1. Le Guide Complet LangGraph
- **Chapitres** : 23
- **Langue** : Français
- **Images** : 120
- **Emplacement** : `data/02-output/Le_Guide_Complet_LangGraph/`

### 2. Apprendre LangChain
- **Chapitres** : 6
- **Langue** : Français
- **Images** : 72
- **Emplacement** : `data/02-output/Apprendre_LangChain/`

## 🎧 Audios

Tous les audios sont pré-générés dans : `data/audio/`

### Structure des fichiers audio :
```
data/audio/
├── Le_Guide_Complet_LangGraph/
│   ├── Le_Guide_Complet_LangGraph_ch00_FULL_*.mp3
│   ├── Le_Guide_Complet_LangGraph_ch01_FULL_*.mp3
│   └── ... (23 chapitres)
└── Apprendre_LangChain/
    ├── Apprendre_LangChain_ch00_FULL_*.mp3
    └── ... (6 chapitres)
```

## 🚀 Utilisation

### Lancer l'application
```bash
cd /Users/alamifaradi/Documents/Programmation/_LivreLLM
python web_app/app.py
```

### Accéder à l'application
Ouvrez votre navigateur : **http://localhost:5001**

### Lire un chapitre
1. Cliquez sur un livre dans la bibliothèque
2. Sélectionnez un chapitre
3. Cliquez sur **"▶ Lire le chapitre"**
4. L'audio démarre automatiquement (déjà généré !)

## 💡 Utilisation hors ligne

✅ **Tous les audios sont pré-générés !**

Vous pouvez maintenant :
- ✅ Écouter tous les chapitres SANS INTERNET
- ✅ Pas d'attente (lecture instantanée)
- ✅ Audios de qualité en français

## 🔄 Régénérer tous les audios

Si besoin de régénérer :
```bash
python scripts/process_all_french_books.py
```

## 📊 Statistiques

- **Total livres** : 2
- **Total chapitres** : 29
- **Total images** : 192
- **Génération audio** : Parallèle (5x plus rapide)
- **Temps génération** : ~15 minutes pour tout

## 🎯 Fonctionnalités

### Chat intelligent
- 💬 Questions sur le chapitre en cours
- 🧠 Contexte de 3000 caractères
- 📝 Historique des 10 derniers messages

### Audio optimisé
- ⚡ Génération 5x plus rapide (parallèle)
- 🎧 Lecture instantanée (pré-généré)
- 💾 Cache intelligent

### Interface moderne
- 📱 Responsive
- 🌐 Navigation fluide
- 🎨 Design épuré

## 📁 Structure du projet

```
_LivreLLM/
├── data/
│   ├── 01-input/          # Fichiers sources (.md)
│   ├── 02-output/         # Livres traités (JSON)
│   └── audio/             # Fichiers audio (MP3)
├── scripts/
│   └── process_all_french_books.py  # Script principal
└── web_app/
    └── app.py             # Application Flask
```

## 🛠️ Commandes utiles

### Vérifier les audios générés
```bash
ls -lh data/audio/Le_Guide_Complet_LangGraph/
```

### Compter les audios
```bash
find data/audio -name "*.mp3" | wc -l
```

### Taille totale des audios
```bash
du -sh data/audio/
```

## ⚠️ Notes importantes

1. **Internet requis UNIQUEMENT pour** :
   - Génération initiale des audios (une seule fois)
   - Réponses du chat (LLM)

2. **Hors ligne disponible pour** :
   - ✅ Lecture des chapitres
   - ✅ Écoute audio
   - ✅ Navigation

3. **Stockage** :
   - Chaque chapitre audio : ~1-5 MB
   - Total estimé : ~150-300 MB

## 🎉 Profitez de votre lecture !

Tous vos livres sont maintenant prêts avec audio pré-généré pour une expérience hors ligne optimale !
