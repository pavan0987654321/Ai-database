import { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';
import { useUser } from '@clerk/clerk-react';
import { getApiUrl } from '../../services/api';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import HelpModal from '../ui/HelpModal';

export default function Layout() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [isHelpOpen, setIsHelpOpen] = useState(false);
    const { user, isLoaded } = useUser();

    // Sync User to Database
    useEffect(() => {
        if (isLoaded && user) {
            fetch(`${getApiUrl()}/sync-user`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    user_id: user.id,
                    email: user.primaryEmailAddress?.emailAddress,
                    full_name: user.fullName
                })
            }).catch(console.error);
        }
    }, [isLoaded, user]);

    return (
        <div className="min-h-screen bg-[var(--bg-base)] transition-theme">
            <Navbar />
            <Sidebar
                collapsed={sidebarCollapsed}
                onToggle={() => setSidebarCollapsed(!sidebarCollapsed)}
                onOpenHelp={() => setIsHelpOpen(true)}
            />
            <HelpModal isOpen={isHelpOpen} onClose={() => setIsHelpOpen(false)} />
            <main className={`pt-12 min-h-screen transition-all duration-300 ${sidebarCollapsed ? 'ml-14' : 'ml-48'}`}>
                <div className="p-5 max-w-[1200px]">
                    <Outlet />
                </div>
            </main>
        </div>
    );
}
