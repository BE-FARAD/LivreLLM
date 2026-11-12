import React, { useState, useEffect, useRef } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';
import styles from './PDFViewer.module.css';
import { ChevronLeft, ChevronRight, ZoomIn, ZoomOut, Play, Pause } from 'lucide-react';
import { type PageData, api } from '../../api/client';

// Configure worker
pdfjs.GlobalWorkerOptions.workerSrc = new URL(
    'pdfjs-dist/build/pdf.worker.min.mjs',
    import.meta.url,
).toString();

interface PDFViewerProps {
    file: string | File;
    pageData?: PageData[];
}

export const PDFViewer: React.FC<PDFViewerProps> = ({ file, pageData }) => {
    const [numPages, setNumPages] = useState<number>(0);
    const [pageNumber, setPageNumber] = useState<number>(1);
    const [scale, setScale] = useState<number>(1.0);

    const [isReading, setIsReading] = useState(false);
    const [currentSentenceIndex, setCurrentSentenceIndex] = useState<number>(-1);
    const audioRef = useRef<HTMLAudioElement | null>(null);

    function onDocumentLoadSuccess({ numPages }: { numPages: number }) {
        setNumPages(numPages);
    }

    const currentPageData = pageData?.find(p => p.page === pageNumber);

    const playSentence = async (index: number) => {
        if (!currentPageData || index >= currentPageData.sentences.length) {
            setIsReading(false);
            setCurrentSentenceIndex(-1);
            return;
        }

        setCurrentSentenceIndex(index);
        const sentence = currentPageData.sentences[index];

        try {
            const audioBlob = await api.getAudio(sentence.text);
            const audioUrl = URL.createObjectURL(audioBlob);

            if (audioRef.current) {
                audioRef.current.src = audioUrl;
                audioRef.current.play();
                audioRef.current.onended = () => {
                    playSentence(index + 1);
                };
            }
        } catch (error) {
            console.error("Failed to play audio", error);
            setIsReading(false);
        }
    };

    const toggleReading = () => {
        if (isReading) {
            setIsReading(false);
            if (audioRef.current) {
                audioRef.current.pause();
            }
        } else {
            setIsReading(true);
            playSentence(currentSentenceIndex === -1 ? 0 : currentSentenceIndex);
        }
    };

    // Cleanup audio on unmount
    useEffect(() => {
        return () => {
            if (audioRef.current) {
                audioRef.current.pause();
            }
        };
    }, []);

    const [error, setError] = useState<Error | null>(null);

    function onDocumentLoadError(err: Error) {
        console.error('Error loading PDF:', err);
        setError(err);
    }

    if (error) {
        return (
            <div className={styles.container} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'red' }}>
                <p>Error loading PDF: {error.message}</p>
            </div>
        );
    }

    return (
        <div className={styles.container}>
            <audio ref={audioRef} style={{ display: 'none' }} />
            <div className={styles.toolbar}>
                <button
                    onClick={() => setPageNumber(prev => Math.max(prev - 1, 1))}
                    disabled={pageNumber <= 1}
                    className={styles.toolButton}
                >
                    <ChevronLeft size={20} />
                </button>
                <span className={styles.pageInfo}>
                    Page {pageNumber} of {numPages}
                </span>
                <button
                    onClick={() => setPageNumber(prev => Math.min(prev + 1, numPages))}
                    disabled={pageNumber >= numPages}
                    className={styles.toolButton}
                >
                    <ChevronRight size={20} />
                </button>

                <div className={styles.divider} />

                <button onClick={() => setScale(s => Math.max(s - 0.1, 0.5))} className={styles.toolButton}>
                    <ZoomOut size={20} />
                </button>
                <span className={styles.scaleInfo}>{Math.round(scale * 100)}%</span>
                <button onClick={() => setScale(s => Math.min(s + 0.1, 2.0))} className={styles.toolButton}>
                    <ZoomIn size={20} />
                </button>

                <div className={styles.divider} />

                <button onClick={toggleReading} className={styles.toolButton} title="Read Aloud">
                    {isReading ? <Pause size={20} /> : <Play size={20} />}
                </button>
            </div>

            <div className={styles.documentContainer}>
                <Document
                    file={file}
                    onLoadSuccess={onDocumentLoadSuccess}
                    onLoadError={onDocumentLoadError}
                    className={styles.document}
                >
                    <div className={styles.pageWrapper}>
                        <Page
                            pageNumber={pageNumber}
                            scale={scale}
                            renderTextLayer={true}
                            renderAnnotationLayer={true}
                        />
                        <div className={styles.overlay}>
                            {currentPageData && currentSentenceIndex !== -1 && currentPageData.sentences[currentSentenceIndex]?.words.map((word, i) => {
                                // Coordinates are usually in PDF points (72 dpi). 
                                // We need to scale them if the PDF is rendered at a different scale.
                                // react-pdf renders at 72dpi * scale by default.
                                // However, PyMuPDF coordinates are also in points.
                                // So we just multiply by scale.
                                // Note: PyMuPDF (0,0) is top-left. react-pdf matches this.
                                const [x0, y0, x1, y1] = word.rect;
                                return (
                                    <div key={i} style={{
                                        position: 'absolute',
                                        left: x0 * scale,
                                        top: y0 * scale,
                                        width: (x1 - x0) * scale,
                                        height: (y1 - y0) * scale,
                                        backgroundColor: 'rgba(255, 255, 0, 0.4)',
                                        pointerEvents: 'none'
                                    }} />
                                );
                            })}
                        </div>
                    </div>
                </Document>
            </div>
        </div>
    );
};
