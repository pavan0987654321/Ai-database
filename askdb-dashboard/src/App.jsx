import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { SignedIn, SignedOut, RedirectToSignIn } from '@clerk/clerk-react';
import Layout from './components/layout/Layout';
import Dashboard from './pages/Dashboard';
import QueryBuilder from './pages/QueryBuilder';
import History from './pages/History';
import Settings from './pages/Settings';
import Login from './pages/Login';
import SignUp from './pages/SignUp';

export default function App() {
  return (
    <ThemeProvider>
      <BrowserRouter>
        <Routes>
          {/* Public Routes for Auth */}
          <Route path="/login/*" element={<Login />} />
          <Route path="/sign-up/*" element={<SignUp />} />

          {/* Protected Main App */}
          <Route
            path="/"
            element={
              <>
                <SignedIn>
                  <Layout />
                </SignedIn>
                <SignedOut>
                  <RedirectToSignIn afterSignOutUrl="/login" />
                </SignedOut>
              </>
            }
          >
            <Route index element={<Dashboard />} />
            <Route path="dashboard" element={<Navigate to="/" replace />} />
            <Route path="queries" element={<QueryBuilder />} />
            <Route path="history" element={<History />} />
            <Route path="settings" element={<Settings />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}
