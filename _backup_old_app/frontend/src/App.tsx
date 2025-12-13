import { useState } from 'react';
import { MacOSWindow } from './components/Layout/MacOSWindow';
import { Book, Plus, Loader2, Mic, X } from 'lucide-react';
import { PDFViewer } from './components/Reader/PDFViewer';
import { api, type BookResponse } from './api/client';
import { ChatPanel } from './components/Chat/ChatPanel';
import VoiceAssistant from './components/VoiceAssistant';
import './index.css';

function App() {
  const [view, setView] = useState<'library' | 'reader'>('library');
  const [currentFile, setCurrentFile] = useState<File | null>(null);
  const [currentBook, setCurrentBook] = useState<BookResponse | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [showVoice, setShowVoice] = useState(false);

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setIsUploading(true);
      try {
        const bookData = await api.uploadBook(file);
        setCurrentBook(bookData);
        setCurrentFile(file);
        setView('reader');

        // Poll for book data
        const pollInterval = setInterval(async () => {
          try {
            const updatedBook = await api.getBook(bookData.id);
            if (updatedBook.pages && updatedBook.pages.length > 0) {
              setCurrentBook(updatedBook);
              clearInterval(pollInterval);
            }
          } catch (e) {
            console.error("Error polling book status", e);
          }
        }, 2000);

      } catch (error) {
        console.error("Upload failed", error);
        alert("Failed to upload book");
      } finally {
        setIsUploading(false);
      }
    }
  };

  return (
    <MacOSWindow sidebarContent={currentBook ? <ChatPanel bookId={currentBook.id} /> : null}>
      {showVoice && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          zIndex: 9999,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          <div style={{ width: '600px', position: 'relative' }}>
            <button
              onClick={() => setShowVoice(false)}
              style={{
                position: 'absolute',
                top: '-40px',
                right: 0,
                background: 'none',
                border: 'none',
                color: 'white',
                cursor: 'pointer'
              }}
            >
              <X size={24} />
            </button>
            <VoiceAssistant />
          </div>
        </div>
      )}

      {view === 'library' ? (
        <div style={{ padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
            <h1 style={{ fontSize: '24px', fontWeight: 600, margin: 0 }}>Library</h1>
            <div style={{ display: 'flex', gap: '10px' }}>
              <button
                onClick={() => setShowVoice(true)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  background: 'var(--mac-accent)',
                  color: 'white',
                  padding: '6px 12px',
                  borderRadius: '6px',
                  fontSize: '13px',
                  fontWeight: 500,
                  border: 'none',
                  cursor: 'pointer'
                }}
              >
                <Mic size={16} />
                Assistant Vocal
              </button>
              <label style={{
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                background: isUploading ? '#ccc' : 'var(--mac-accent)',
                color: 'white',
                padding: '6px 12px',
                borderRadius: '6px',
                fontSize: '13px',
                fontWeight: 500,
                cursor: isUploading ? 'wait' : 'pointer',
                transition: 'background-color 0.2s'
              }}>
                {isUploading ? <Loader2 size={16} className="animate-spin" style={{ animation: 'spin 1s linear infinite' }} /> : <Plus size={16} />}
                {isUploading ? 'Uploading...' : 'Add Book'}
                <input type="file" accept=".pdf" onChange={handleFileChange} style={{ display: 'none' }} disabled={isUploading} />
              </label>
            </div>
          </div>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(150px, 1fr))',
            gap: '24px'
          }}>
            {/* Placeholder Books */}
            {[1, 2, 3].map((i) => (
              <div key={i} style={{
                display: 'flex',
                flexDirection: 'column',
                gap: '8px',
                cursor: 'pointer',
                opacity: 0.6
              }}>
                <div style={{
                  aspectRatio: '2/3',
                  backgroundColor: '#e5e5e5',
                  borderRadius: '8px',
                  boxShadow: 'var(--shadow-md)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  <Book size={32} color="var(--mac-text-secondary)" />
                </div>
                <span style={{ fontSize: '13px', fontWeight: 500 }}>Sample Book {i}</span>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
          <div style={{
            height: '40px',
            borderBottom: '1px solid var(--mac-divider)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '0 16px',
            background: 'white'
          }}>
            <button
              onClick={() => setView('library')}
              style={{
                background: 'none',
                border: 'none',
                color: 'var(--mac-accent)',
                fontSize: '13px',
                fontWeight: 500,
                cursor: 'pointer'
              }}
            >
              Back to Library
            </button>
            <button
              onClick={() => setShowVoice(true)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                background: 'none',
                color: 'var(--mac-accent)',
                fontSize: '13px',
                fontWeight: 500,
                border: 'none',
                cursor: 'pointer'
              }}
            >
              <Mic size={16} />
              Assistant Vocal
            </button>
          </div>
          <div style={{ flex: 1, overflow: 'hidden' }}>
            {currentFile ? (
              <>
                <PDFViewer file={currentFile} pageData={currentBook?.pages} />
                {(!currentBook?.pages || currentBook.pages.length === 0) && (
                  <div style={{
                    position: 'absolute',
                    bottom: '20px',
                    right: '20px',
                    background: 'rgba(0,0,0,0.7)',
                    color: 'white',
                    padding: '10px 20px',
                    borderRadius: '20px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '10px',
                    fontSize: '14px',
                    backdropFilter: 'blur(10px)'
                  }}>
                    <Loader2 size={16} className="animate-spin" style={{ animation: 'spin 1s linear infinite' }} />
                    Analyzing book content...
                  </div>
                )}
              </>
            ) : (
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                No file selected
              </div>
            )}
          </div>
        </div>
      )}
    </MacOSWindow>
  );
}

export default App;
