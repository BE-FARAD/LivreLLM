import React, { useState } from 'react';
import { Send } from 'lucide-react';
import { api } from '../../api/client';
import styles from './ChatPanel.module.css';

interface ChatPanelProps {
    bookId: string;
}

interface Message {
    role: 'user' | 'assistant';
    content: string;
}

export const ChatPanel: React.FC<ChatPanelProps> = ({ bookId }) => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSend = async () => {
        if (!input.trim() || isLoading) return;

        const userMessage = input;
        setInput('');
        setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
        setIsLoading(true);

        try {
            const response = await api.chat(userMessage, bookId);
            setMessages(prev => [...prev, { role: 'assistant', content: response.answer }]);
        } catch (error) {
            console.error("Chat failed", error);
            setMessages(prev => [...prev, { role: 'assistant', content: "Sorry, I encountered an error." }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className={styles.container}>
            <div className={styles.messages}>
                {messages.length === 0 && (
                    <div className={styles.emptyState}>
                        Ask me anything about the book!
                    </div>
                )}
                {messages.map((msg, i) => (
                    <div key={i} className={`${styles.message} ${styles[msg.role]}`}>
                        {msg.content}
                    </div>
                ))}
                {isLoading && <div className={styles.loading}>Thinking...</div>}
            </div>
            <div className={styles.inputArea}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Ask a question..."
                    className={styles.input}
                />
                <button onClick={handleSend} disabled={isLoading} className={styles.sendButton}>
                    <Send size={16} />
                </button>
            </div>
        </div>
    );
};
