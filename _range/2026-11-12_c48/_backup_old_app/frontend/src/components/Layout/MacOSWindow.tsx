import React from 'react';
import { Book, Search, Settings, MessageSquare } from 'lucide-react';
import styles from './MacOSWindow.module.css';
import clsx from 'clsx';

interface MacOSWindowProps {
    children: React.ReactNode;
    sidebarContent?: React.ReactNode;
}

export const MacOSWindow: React.FC<MacOSWindowProps> = ({ children, sidebarContent }) => {
    return (
        <div className={styles.window}>
            <div className={styles.titlebar}>
                <div className={styles.trafficLights}>
                    <div className={clsx(styles.trafficLight, styles.close)} />
                    <div className={clsx(styles.trafficLight, styles.minimize)} />
                    <div className={clsx(styles.trafficLight, styles.maximize)} />
                </div>
                <div className={styles.toolbar}>
                    {/* Toolbar items can go here */}
                </div>
            </div>

            <div className={styles.content}>
                <aside className={styles.sidebar}>
                    <div className={styles.sidebarSection}>
                        <h3 className={styles.sidebarTitle}>Library</h3>
                        <nav className={styles.nav}>
                            <a href="#" className={clsx(styles.navItem, styles.active)}>
                                <Book size={18} />
                                <span>All Books</span>
                            </a>
                            <a href="#" className={styles.navItem}>
                                <Search size={18} />
                                <span>Search</span>
                            </a>
                        </nav>
                    </div>

                    <div className={styles.sidebarSection}>
                        <h3 className={styles.sidebarTitle}>Assistant</h3>
                        <nav className={styles.nav}>
                            <a href="#" className={styles.navItem}>
                                <MessageSquare size={18} />
                                <span>Chat</span>
                            </a>
                        </nav>
                    </div>

                    {sidebarContent}

                    <div className={styles.sidebarSpacer} />

                    <div className={styles.sidebarSection}>
                        <nav className={styles.nav}>
                            <a href="#" className={styles.navItem}>
                                <Settings size={18} />
                                <span>Settings</span>
                            </a>
                        </nav>
                    </div>
                </aside>

                <main className={styles.main}>
                    {children}
                </main>
            </div>
        </div>
    );
};
