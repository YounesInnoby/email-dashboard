import React from "react";
import { Mail, User, Clock } from "lucide-react";

export interface EmailBase {
  id: string;
  subject: string;
  sender: string;
  body?: string;
  pdf_attachment?: string;
  pdf_text?: string;
  timestamp?: string;
  status?: "unbearbeitet" | "in_bearbeitung" | "bearbeitet";
}

export interface EmailWithResponse extends EmailBase {
  response?: {
    Kunde: string;
    Datum: string;
    Positionen: any[];
  };
}

interface Props {
  onSelectEmail: (email: EmailWithResponse | null) => void;
  emails: EmailWithResponse[];
}

const EmailList: React.FC<Props> = ({ onSelectEmail, emails }) => {
  const [selectedId, setSelectedId] = React.useState<string | null>(null);

  return (
    <div className="w-80 bg-white shadow-lg h-screen overflow-y-auto p-4 border-r">
      <h2 className="text-xl font-semibold mb-4 flex items-center">
        <Mail className="h-6 w-6 mr-2 text-gray-600" /> Eingang
      </h2>

      {emails.length === 0 ? (
        <p className="text-gray-600">Keine E-Mails gefunden</p>
      ) : (
        <div className="space-y-2">
          {emails.map((email) => (
            <div
              key={email.id}
              onClick={() => {
                setSelectedId(email.id);
                onSelectEmail(email);
              }}
              className={`p-4 rounded-md border shadow cursor-pointer transition ${
                selectedId === email.id
                  ? "bg-blue-200 border-blue-600"
                  : "hover:bg-gray-200"
              }`}
            >
              <div className="flex justify-between items-center">
                <h3 className="truncate font-semibold">{email.subject}</h3>
                <span className="text-xs text-gray-500 flex items-center">
                  <Clock className="h-4 w-4 mr-1" /> {email.timestamp ?? "–"}
                </span>
              </div>

              <p className="text-sm text-gray-700 flex items-center">
                <User className="h-4 w-4 mr-2" /> {email.sender}
              </p>

              <div className="mt-2 flex justify-end">
                <span
                  className={`text-xs font-semibold px-2 py-1 rounded-full shadow ${
                    email.status === "bearbeitet"
                      ? "bg-green-100 text-green-800"
                      : email.status === "in_bearbeitung"
                      ? "bg-yellow-100 text-yellow-800"
                      : "bg-red-100 text-red-800"
                  }`}
                >
                  {email.status || "unbearbeitet"}
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default EmailList;
