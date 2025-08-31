import { EmailWithResponse } from "../types";
import { ExternalLink, MoreVertical, AlertTriangle } from "lucide-react";

type FileItemProps = {
  email: EmailWithResponse;
  selected: boolean;
  onClick: () => void;
  compact?: boolean;
};

export default function FileItem({ email, selected, onClick, compact = false }: FileItemProps) {
  const { subject, id, status } = email;

  // Warnung nur für Bestellungen mit action_required
  const showWarning = status === "action_required" && email.Kategorie === "Bestellung";

  return (
    <div
      className={`mb-2 rounded-md cursor-pointer transition ${
        selected ? "bg-green-50 shadow-md" : "hover:bg-gray-100 hover:shadow-sm hover:-translate-y-0.5"
      }`}
      onClick={onClick}
    >
      {/* 4-Spalten-Zeile (bleibt ausgerichtet zu den Headern) */}
      <div
        className={`grid grid-cols-[minmax(0,1fr)_300px_200px_40px] items-center ${
          compact ? "py-2 px-3" : "py-4 px-5"
        }`}
      >
        {/* File (Spalte 1) */}
        <div className="truncate">
          <div className="font-medium text-[15px] leading-tight truncate">{subject}</div>
          <div className="text-sm text-gray-500 truncate">{`email_${id}.pdf`}</div>
        </div>

        {/* Status (Spalte 2) */}
        <div className="flex items-center h-full">
          <span
            className={`inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-full ${
              status === "bearbeitet"
                ? "bg-green-100 text-green-800"
                : status === "in_bearbeitung"
                ? "bg-yellow-100 text-yellow-800"
                : status === "action_required"
                ? "bg-red-100 text-red-800"
                : "bg-gray-100 text-gray-800"
            }`}
          >
            <span className="w-2 h-2 rounded-full bg-current" />
            {status}
          </span>
        </div>

        {/* Received at (Spalte 3) */}
        <div className="flex items-center h-full text-sm text-gray-500">
          {email.response?.Datum ? new Date(email.response.Datum).toLocaleDateString() : "–"}
        </div>

        {/* Actions (Spalte 4) */}
        <div className="flex justify-end gap-2 text-gray-500">
          <button
            title="Open in new tab"
            onClick={(e) => {
              e.stopPropagation();
              window.open(`/documents/${id}`, "_blank");
            }}
          >
            <ExternalLink size={16} />
          </button>
          <button title="More options" onClick={(e) => e.stopPropagation()}>
            <MoreVertical size={16} />
          </button>
        </div>
      </div>

      {/* Warnbox unter der Zeile (volle Breite, zerstört das Grid nicht) */}
      {showWarning && (
        <div className={`${compact ? "px-3" : "px-5"} pb-4`}>
          <div className="rounded-md border border-red-200 bg-red-50 text-red-800 p-3 flex items-center gap-3">
            <AlertTriangle className="shrink-0" size={16} />
            <span className="text-sm">
              Lagerbestand nicht verfügbar für Pos. 10, Ermeto-Rohr V2A 22x2,0mm – Nur noch 5 Artikel auf Lager!
            </span>
            <button
              onClick={(e) => {
                e.stopPropagation();
                alert("Bestellvorgang initiiert!");
              }}
              className="ml-auto bg-red-600 hover:bg-red-700 text-white text-sm px-3 py-1 rounded"
            >
              Bestellvorgang initiieren
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
