import React, { useState } from "react";
import { ChevronUp, ChevronDown, Plus } from "lucide-react";
import type { EmailWithResponse } from "./EmailList";

interface Props {
  emailWithResponse: EmailWithResponse | null;
  onMarkAsDone: (id: string, newStatus: "bearbeitet") => void;
}


const EmailViewer: React.FC<Props> = ({ emailWithResponse, onMarkAsDone }) => {
  const [showPdfText, setShowPdfText] = useState(false);
  const [positions, setPositions] = useState(emailWithResponse?.response?.Positionen ?? []);

  React.useEffect(() => {
    setPositions(emailWithResponse?.response?.Positionen ?? []);
  }, [emailWithResponse]);

  if (!emailWithResponse)
    return <div className="flex justify-center items-center h-full text-gray-500">📩 Wähle eine E‑Mail aus</div>;

  const email = emailWithResponse;
  const metaFields = { ...(emailWithResponse.response ?? {}) };
  delete metaFields.Positionen;


  const handleAdd = () => {
    const nextIdx = positions.length + 1;
    const clone = { ...positions[0], Position: nextIdx };
    setPositions([...positions, clone]);
  };

  const handleChange = (i: number, key: string, value: any) => {
    const copy = [...positions];
    copy[i][key] = isNaN(copy[i][key]) ? value : Number(value);
    setPositions(copy);
  };



  return (
    <div className="flex gap-6 p-6 h-full">
      {/* Links */}
      <div className="w-1/2 bg-white shadow rounded p-6 overflow-y-auto max-h-screen">
        <h2 className="text-2xl font-bold mb-2">{email.subject}</h2>
        <p className="text-gray-600 mb-4">Von: {email.sender}</p>
        <hr className="mb-4" />
        {email.body ? <p>{email.body}</p> : <p className="text-gray-500">Kein Inhalt verfügbar</p>}
        {email.pdf_attachment && (
          <div className="mt-6 border p-4 rounded bg-gray-50">
            <h3 className="font-semibold mb-2">📎 Anhang</h3>
            <iframe className="w-full h-[700px] mb-2" src={`data:application/pdf;base64,${email.pdf_attachment}`} />
            <a href={`data:application/pdf;base64,${email.pdf_attachment}`} download={`email_${email.id}.pdf`} className="text-blue-600">📥 Herunterladen</a>
          </div>
        )}
        {email.pdf_text && (
          <div className="mt-4 border p-4 rounded bg-gray-100">
            <button className="w-full flex justify-between items-center" onClick={() => setShowPdfText(!showPdfText)}>
              <span>📄 Extrahierter Text</span>
              {showPdfText ? <ChevronUp /> : <ChevronDown />}
            </button>
            {showPdfText && <div className="mt-2 whitespace-pre-line max-h-64 overflow-auto">{email.pdf_text}</div>}
          </div>
        )}
      </div>

      {/* Rechts */}
      <div className="w-1/2 overflow-y-auto max-h-screen">
        <h3 className="text-xl font-semibold mb-4">📋 Allgemeine Informationen</h3>
          <div className="mb-6 p-4 border rounded bg-gray-100">
            {Object.entries(metaFields).map(([key, value]) => (
              <div key={key} className="mb-2">
                <label className="block text-sm font-medium text-gray-700">{key}</label>
                <input className="mt-1 w-full border rounded p-1 bg-white" value={value as any} readOnly />
              </div>
            ))}
          </div>
        <h3 className="text-xl font-semibold mb-4">Positionen aus JSON</h3>
        {positions.map((pos, i) => (
          <div key={i} className="mb-6 p-4 border rounded bg-gray-50">
            <h4 className="font-bold mb-2">Position {pos.Position}</h4>
            {Object.entries(pos).map(([k, v]) => (
              <div key={k} className="mb-2">
                <label className="block text-sm font-medium text-gray-700">{k}</label>
                <input
                  className="mt-1 w-full border rounded p-1"
                  value={v as any}
                  onChange={(e) => handleChange(i, k, e.target.value)}
                />
              </div>
            ))}
          </div>
        ))}
        <button onClick={handleAdd} className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          <Plus /> Neue Position
        </button>
          <button
            onClick={() => {
              if (emailWithResponse) {
                onMarkAsDone(emailWithResponse.id, "bearbeitet");
              }
            }}
            className="mt-4 bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded"
          >
            ✅ Speichern & Beenden
          </button>

      </div>




    </div>


  );


};

export default EmailViewer;
