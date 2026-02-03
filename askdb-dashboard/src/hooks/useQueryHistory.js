import { useState, useEffect, useCallback } from 'react';

const STORAGE_KEY = 'queryflow_query_history';
const MAX_HISTORY = 100; // Keep last 100 queries

/**
 * Custom hook for managing query history
 */
export default function useQueryHistory() {
    const [history, setHistory] = useState([]);

    // Load history from localStorage on mount
    useEffect(() => {
        try {
            const stored = localStorage.getItem(STORAGE_KEY);
            if (stored) {
                const parsed = JSON.parse(stored);
                setHistory(parsed);
            }
        } catch (error) {
            console.warn('Failed to load query history:', error);
        }
    }, []);

    // Save history to localStorage whenever it changes
    useEffect(() => {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
        } catch (error) {
            console.warn('Failed to save query history:', error);
        }
    }, [history]);

    // Add a query to history
    const addToHistory = useCallback((query, status, executionTime, rows = 0, sql = '') => {
        const newEntry = {
            id: Date.now(),
            query,
            status, // 'success' or 'error'
            executionTime,
            rows,
            sql,
            timestamp: new Date().toISOString(),
        };

        setHistory(prev => {
            const updated = [newEntry, ...prev];
            // Keep only the last MAX_HISTORY entries
            return updated.slice(0, MAX_HISTORY);
        });

        return newEntry;
    }, []);

    // Clear all history
    const clearHistory = useCallback(() => {
        setHistory([]);
        localStorage.removeItem(STORAGE_KEY);
    }, []);

    // Delete a specific entry
    const deleteEntry = useCallback((id) => {
        setHistory(prev => prev.filter(entry => entry.id !== id));
    }, []);

    // Get formatted time ago
    const getTimeAgo = useCallback((timestamp) => {
        const now = new Date();
        const then = new Date(timestamp);
        const diffMs = now - then;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins} min ago`;
        if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
        if (diffDays === 1) return 'Yesterday';
        if (diffDays < 7) return `${diffDays} days ago`;
        return then.toLocaleDateString();
    }, []);

    return {
        history,
        addToHistory,
        clearHistory,
        deleteEntry,
        getTimeAgo,
    };
}
