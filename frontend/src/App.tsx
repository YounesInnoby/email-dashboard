import React, { useState, useEffect } from "react";
import axios from "axios";
import EmailList, { EmailWithResponse } from "./components/EmailList";
import EmailViewer from "./components/EmailViewer";
import { Mail, Bell, LogOut } from "lucide-react";

const App: React.FC = () => {
  const [selectedEmail, setSelectedEmail] = useState<EmailWithResponse | null>(null);
  const [emailList, setEmailList] = useState<EmailWithResponse[]>([]);
  const baseURL = `${window.location.protocol}//${window.location.hostname}:8001`;

    useEffect(() => {
    axios.get<EmailWithResponse[]>(`${baseURL}/emails`)
      .then(res => setEmailList(res.data))
      .catch(err => console.error("📭 Fehler beim Laden der E-Mails:", err));
  }, []);

  // Wird von EmailList verwendet
  const handleSelectEmail = (email: EmailWithResponse | null) => {
    setSelectedEmail(email);
  };

  // Wird vom EmailViewer aufgerufen
  const updateEmailStatus = (id: string, newStatus: "bearbeitet") => {
    setEmailList(prev =>
      prev.map(e => (e.id === id ? { ...e, status: newStatus } : e))
    );
    if (selectedEmail?.id === id) {
      setSelectedEmail({ ...selectedEmail, status: newStatus });
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-gray-900 text-white flex flex-col p-4">
        <h1 className="text-2xl font-bold mb-6">📬 Postfach</h1>
        <nav className="flex flex-col space-y-2">
          <button className="p-3 bg-gray-700 rounded-lg hover:bg-gray-600">📥 Eingang</button>
          <button className="p-3 bg-gray-700 rounded-lg hover:bg-gray-600">📤 Gesendet</button>
          <button className="p-3 bg-gray-700 rounded-lg hover:bg-gray-600">🗑️ Papierkorb</button>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex flex-col flex-grow">
        <div className="bg-blue-500 p-4 flex justify-between items-center shadow-md">
          <h2 className="text-xl text-white font-bold flex items-center">
            <Mail className="h-6 w-6 mr-2" /> Posteingang
          </h2>
          <div className="flex items-center space-x-4">
            <input type="text" placeholder="Suche..." className="p-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-white bg-blue-600 text-white placeholder-white" />
            <button className="p-2 bg-blue-700 text-white rounded-lg hover:bg-blue-800"><Bell className="h-5 w-5" /></button>
            <button className="p-2 bg-gray-800 text-white rounded-lg hover:bg-gray-700"><LogOut className="h-5 w-5" /></button>
          </div>
        </div>

        <div className="flex flex-grow overflow-hidden">
          <EmailList emails={emailList} onSelectEmail={handleSelectEmail} />
          <div className="flex-grow overflow-y-auto">
            <EmailViewer emailWithResponse={selectedEmail} onMarkAsDone={updateEmailStatus} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
