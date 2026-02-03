import { useState, useEffect, useCallback } from 'react';

const STORAGE_KEY = 'queryflow_session_metrics';

/**
 * Custom hook for tracking session-based metrics
 * Provides honest, demo-appropriate analytics
 */
export default function useSessionMetrics() {
    const [metrics, setMetrics] = useState({
        totalQueries: 0,
        successfulQueries: 0,
        queryTimes: [],
    });

    // Load metrics from localStorage on mount
    useEffect(() => {
        try {
            const stored = localStorage.getItem(STORAGE_KEY);
            if (stored) {
                const parsed = JSON.parse(stored);
                setMetrics(parsed);
            }
        } catch (error) {
            console.warn('Failed to load session metrics:', error);
        }
    }, []);

    // Save metrics to localStorage whenever they change
    useEffect(() => {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(metrics));
        } catch (error) {
            console.warn('Failed to save session metrics:', error);
        }
    }, [metrics]);

    // Record a query execution
    const recordQuery = useCallback((success, executionTime) => {
        setMetrics(prev => ({
            totalQueries: prev.totalQueries + 1,
            successfulQueries: success ? prev.successfulQueries + 1 : prev.successfulQueries,
            queryTimes: [...prev.queryTimes, executionTime],
        }));
    }, []);

    // Calculate average query time
    const getAverageTime = useCallback(() => {
        if (metrics.queryTimes.length === 0) return 0;
        const sum = metrics.queryTimes.reduce((acc, time) => acc + time, 0);
        return Math.round(sum / metrics.queryTimes.length);
    }, [metrics.queryTimes]);

    // Reset all metrics (for new session)
    const resetMetrics = useCallback(() => {
        setMetrics({
            totalQueries: 0,
            successfulQueries: 0,
            queryTimes: [],
        });
        localStorage.removeItem(STORAGE_KEY);
    }, []);

    return {
        totalQueries: metrics.totalQueries,
        successfulQueries: metrics.successfulQueries,
        averageTime: getAverageTime(),
        recordQuery,
        resetMetrics,
    };
}
