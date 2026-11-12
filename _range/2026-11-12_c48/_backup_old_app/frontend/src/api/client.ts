import axios from 'axios';

const API_URL = 'http://localhost:8000';

export interface Word {
    text: string;
    rect: [number, number, number, number];
}

export interface Sentence {
    text: string;
    words: Word[];
}

export interface PageData {
    page: number;
    width: number;
    height: number;
    sentences: Sentence[];
}

export interface BookResponse {
    id: string;
    title: string;
    pages: PageData[];
}

export interface ChatResponse {
    answer: string;
    sources: string[];
}

export const api = {
    uploadBook: async (file: File): Promise<BookResponse> => {
        const formData = new FormData();
        formData.append('file', file);
        const response = await axios.post(`${API_URL}/books/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    },

    getBook: async (bookId: string): Promise<BookResponse> => {
        const response = await axios.get(`${API_URL}/books/${bookId}`);
        return response.data;
    },

    chat: async (question: string, bookId: string): Promise<ChatResponse> => {
        const response = await axios.post(`${API_URL}/chat/`, {
            question,
            book_id: bookId
        });
        return response.data;
    },

    getAudio: async (text: string): Promise<Blob> => {
        const response = await axios.post(`${API_URL}/tts/`, { text }, {
            responseType: 'blob'
        });
        return response.data;
    }
};
