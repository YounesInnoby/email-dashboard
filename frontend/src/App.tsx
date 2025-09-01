// src/App.tsx
import React, { useEffect, useMemo, useState, ReactNode } from "react";
import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import FileItem from "./components/FileItem";
import DetailModal from "./components/DetailModal";
import type { EmailWithResponse } from "./types";
import TopBar from "./components/TopBar";
import HeaderActions from "./components/HeaderActions";
import Login from "./pages/Login";
import { GlobalMenuProvider } from "./context/GlobalMenuContext";

// --- Kategorien-Tabs (Sidebar)
type TabKey = "client-request" | "order" | "invoice";
// --- Status-Tabs (TopBar)
type StatusTab = "inbox" | "bearbeitet" | "in_bearbeitung" | "action_required";

const mapKategorieToTab = (k: EmailWithResponse["Kategorie"]): TabKey => {
  switch (k) {
    case "Kundenanfrage":
      return "client-request";
    case "Bestellung":
      return "order";
    case "Rechnung":
      return "invoice";
    default:
      return "order";
  }
};

// ---------- Mini ErrorBoundary ----------
class ErrorBoundary extends React.Component<{ children: React.ReactNode }, { hasError: boolean; err?: any }> {
  constructor(props: any) {
    super(props);
    this.state = { hasError: false, err: null };
  }
  static getDerivedStateFromError(err: any) {
    return { hasError: true, err };
  }
  componentDidCatch(err: any) {
    console.error("App crashed:", err);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: 24, fontFamily: "system-ui" }}>
          <h2>Unerwarteter Fehler</h2>
          <pre style={{ whiteSpace: "pre-wrap" }}>{String(this.state.err)}</pre>
        </div>
      );
    }
    return this.props.children;
  }
}

// ---------- Minimaler Guard ----------
function ProtectedRoute({ children }: { children: ReactNode }) {
  const location = useLocation();
  const token = typeof window !== "undefined" ? localStorage.getItem("token") : null;
  if (!token) return <Navigate to="/login" replace state={{ from: location }} />;
  return <>{children}</>;
}

// ---------- Dein bisheriges Layout (AppShell) ----------
function AppShell() {
  const [emails, setEmails] = useState<EmailWithResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selected, setSelected] = useState<EmailWithResponse | null>(null);

  const [activeTab, setActiveTab] = useState<TabKey>("client-request");
  const [statusTab, setStatusTab] = useState<StatusTab>("inbox");

  useEffect(() => {
    (async () => {
      try {
        // relative URL -> funktioniert lokal, per Domain und via ngrok
        const res = await fetch("/emails");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setEmails(data as EmailWithResponse[]);
      } catch (e: any) {
        setError(e.message || "Fehler beim Laden");
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const counts = useMemo(() => {
    const base: Record<TabKey, number> = { "client-request": 0, order: 0, invoice: 0 };
    for (const mail of emails) base[mapKategorieToTab(mail.Kategorie)] += 1;
    return base;
  }, [emails]);

  const filteredByCategory = useMemo(
    () => emails.filter((m) => mapKategorieToTab(m.Kategorie) === activeTab),
    [emails, activeTab]
  );

  const statusCounts = useMemo(() => ({
    inbox: filteredByCategory.length,
    bearbeitet: filteredByCategory.filter((e) => e.status === "bearbeitet").length,
    in_bearbeitung: filteredByCategory.filter((e) => e.status === "in_bearbeitung").length,
    action_required: filteredByCategory.filter((e) => e.status === "action_required").length,
  }), [filteredByCategory]);

  const filtered = useMemo(() => (
    statusTab === "inbox" ? filteredByCategory : filteredByCategory.filter((m) => m.status === statusTab)
  ), [filteredByCategory, statusTab]);

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar active={activeTab} counts={counts} onChange={setActiveTab} />
      <div className="flex flex-col flex-1">
        <main className="flex-1 p-6 overflow-y-auto">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-2xl font-semibold text-gray-800">
              {activeTab === "client-request" ? "Client Requests" : activeTab === "order" ? "Orders" : "Invoices"}
            </h1>
            <HeaderActions />
          </div>

          <TopBar activeTab={statusTab} onChange={setStatusTab} counts={statusCounts} />

          <div className="bg-gray-100 rounded-md overflow-hidden shadow-sm">
            <div className="grid grid-cols-[minmax(0,1fr)_300px_200px_40px] text-sm font-medium text-gray-500 bg-gray-200 py-2 px-4">
              <span>File</span>
              <span>Status</span>
              <span>Received at</span>
              <span></span>
            </div>

            {loading && <div className="p-4 text-center text-gray-600">Lade E-Mails…</div>}
            {error && <div className="p-4 text-center text-red-600">Fehler: {error}</div>}
            {!loading && !error && filtered.length === 0 && (
              <div className="p-4 text-center text-gray-600">Keine Einträge in dieser Kategorie / diesem Status.</div>
            )}

            {!loading && filtered.map((email) => (
              <FileItem
                key={email.id}
                email={email}
                selected={selected?.id === email.id}
                onClick={() => setSelected(email)}
                compact
              />
            ))}
          </div>
        </main>
        {selected && <DetailModal email={selected} onClose={() => setSelected(null)} />}
      </div>
    </div>
  );
}

// ---------- Oberste App OHNE BrowserRouter (der kommt in index.tsx) ----------
export default function App() {
  const NotFoundRedirect = () => {
    const hasToken = typeof window !== "undefined" && !!localStorage.getItem("token");
    return <Navigate to={hasToken ? "/" : "/login"} replace />;
  };

  return (
    <ErrorBoundary>
      <GlobalMenuProvider>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<ProtectedRoute><AppShell /></ProtectedRoute>} />
          <Route path="*" element={<NotFoundRedirect />} />
        </Routes>
      </GlobalMenuProvider>
    </ErrorBoundary>
  );
}
