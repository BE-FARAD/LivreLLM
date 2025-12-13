// Load chapters on page load
window.addEventListener('DOMContentLoaded', async () => {
    await loadChapters();
});

async function loadChapters() {
    try {
        const response = await fetch(`/api/book/${bookName}/chapters`);
        const data = await response.json();

        chapters = data.chapters;

        const chapterList = document.getElementById('chapter-list');
        chapterList.innerHTML = '';

        chapters.forEach((chapter, index) => {
            const item = document.createElement('div');
            item.className = 'chapter-item';
            item.textContent = `${chapter.number}. ${chapter.title}`;
            item.onclick = () => loadChapter(chapter.number);
            chapterList.appendChild(item);
        });

        // Load first chapter by default
        if (chapters.length > 0) {
            loadChapter(chapters[0].number);
        }
    } catch (error) {
        console.error('Error loading chapters:', error);
    }
}

async function loadChapter(chapterNum) {
    try {
        const response = await fetch(`/api/book/${bookName}/chapter/${chapterNum}`);
        const chapter = await response.json();

        currentChapter = chapter;

        // Update title
        document.getElementById('chapter-title').textContent = chapter.title;

        // Render content
        const contentDiv = document.getElementById('chapter-content');
        contentDiv.innerHTML = '';

        chapter.paragraphs.forEach(para => {
            if (para.content.startsWith('![](')) {
                // Image
                const imageName = para.content.slice(4, -1);
                const img = document.createElement('img');
                img.src = `/images/${bookName}/${imageName}`;
                img.alt = imageName;
                img.className = 'chapter-image';
                contentDiv.appendChild(img);
            } else {
                // Text paragraph
                const p = document.createElement('div');
                p.className = 'paragraph';
                p.innerHTML = marked.parse(para.content); // Using marked.js for markdown
                contentDiv.appendChild(p);
            }
        });

        // Highlight active chapter by finding it by number
        document.querySelectorAll('.chapter-item').forEach((item, idx) => {
            item.classList.remove('active');
            if (chapters[idx] && chapters[idx].number === chapterNum) {
                item.classList.add('active');
            }
        });

        // Reset audio
        document.getElementById('chapter-audio').style.display = 'none';

    } catch (error) {
        console.error('Error loading chapter:', error);
    }
}

// Play Chapter Audio - SMART PLAY/PAUSE
document.getElementById('play-chapter').addEventListener('click', () => {
    if (!currentChapter) return;

    const btn = document.getElementById('play-chapter');
    const audioPlayer = document.getElementById('chapter-audio');

    // Construct target URL (ignoring domain for comparison)
    const audioPath = `/audio/${bookName}/chapter/${currentChapter.number}/file`;

    // Check if this specific audio is already loaded
    const isSameAudio = audioPlayer.src.includes(audioPath) || (audioPlayer.currentSrc && audioPlayer.currentSrc.includes(audioPath));
    const isReady = audioPlayer.readyState >= 1; // HAVE_METADATA or better

    if (isSameAudio && isReady) {
        // Audio is already loaded, just toggle play/pause
        if (audioPlayer.paused) {
            audioPlayer.play().then(() => {
                btn.textContent = '🎧 Audio en cours (Pause ||)';
            }).catch(err => {
                console.error("Play error:", err);
                btn.textContent = '⚠️ Erreur lecture';
            });
        } else {
            audioPlayer.pause();
            btn.textContent = '✅ Audio prêt - Reprendre ▶';
        }
        return;
    }

    // --- INITIAL LOAD ---
    btn.textContent = '⏳ Chargement...';
    console.log('[AUDIO] Loading new:', audioPath);

    audioPlayer.src = audioPath;
    audioPlayer.style.display = 'block';
    audioPlayer.controls = true;
    audioPlayer.load();

    btn.textContent = '✅ Audio prêt - Cliquez ▶';

    // Try auto-play
    audioPlayer.play().then(() => {
        btn.textContent = '🎧 Audio en cours (Pause ||)';
    }).catch(err => {
        console.log('[AUDIO] Autoplay prevented, waiting for user click');
        btn.textContent = '✅ Audio prêt - Cliquez ▶';
    });
});

// Update button state on standard events
const audioPlayer = document.getElementById('chapter-audio');
audioPlayer.addEventListener('play', () => {
    const btn = document.getElementById('play-chapter');
    btn.textContent = '🎧 Audio en cours (Pause ||)';
});
audioPlayer.addEventListener('pause', () => {
    const btn = document.getElementById('play-chapter');
    btn.textContent = '✅ Audio prêt - Reprendre ▶';
});
audioPlayer.addEventListener('ended', () => {
    const btn = document.getElementById('play-chapter');
    btn.textContent = '↻ Recommencer le chapitre';
});

// Chat with history
let chatHistory = [];

document.getElementById('chat-send').addEventListener('click', async () => {
    await sendChatMessage();
});

document.getElementById('chat-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendChatMessage();
    }
});

async function sendChatMessage() {
    const input = document.getElementById('chat-input');
    const question = input.value.trim();

    if (!question || !currentChapter) return;

    // Add user message to UI
    addChatMessage('user', question);
    chatHistory.push({ role: 'user', content: question });
    input.value = '';

    // Show typing indicator
    const typingId = addChatMessage('assistant', '💬 Réflexion en cours...');

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question: question,
                book_name: bookName,
                chapter_num: currentChapter.number,
                history: chatHistory
            })
        });

        const data = await response.json();

        // Remove typing indicator
        document.getElementById(typingId)?.remove();

        if (data.answer) {
            addChatMessage('assistant', data.answer);
            chatHistory.push({ role: 'assistant', content: data.answer });
        } else {
            addChatMessage('assistant', '❌ Erreur lors de la réponse');
        }
    } catch (error) {
        console.error('Error sending chat:', error);
        document.getElementById(typingId)?.remove();
        addChatMessage('assistant', '❌ Erreur de connexion');
    }
}

function addChatMessage(role, content) {
    const messagesDiv = document.getElementById('chat-messages');
    const msg = document.createElement('div');
    const msgId = `msg-${Date.now()}-${Math.random()}`;
    msg.id = msgId;
    msg.className = `chat-message ${role}`;
    msg.textContent = content;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    return msgId;
}
