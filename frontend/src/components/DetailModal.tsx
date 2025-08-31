import {
  Pencil,
} from "lucide-react";
import { useState } from "react";
import WorkistSidebar from "./WorkistSidebar";
import type { EmailWithResponse } from "../types";
import PDFTopbar from "./PDFTopbar";


interface Props {
  email: EmailWithResponse;
  onClose: () => void;
}

export default function DetailModal({ email, onClose }: Props) {
  const [editHeader, setEditHeader] = useState(false);
  const [editPosition, setEditPosition] = useState<number | null>(null);

  // Helpers oben in DetailModal.tsx
    const fmtScore = (s?: number) =>
      typeof s === "number" ? `${Math.round(s * 100)}%` : "–";

    const scoreColor = (s?: number) => {
      if (typeof s !== "number") return "bg-gray-100 text-gray-600";
      if (s >= 0.9) return "bg-green-100 text-green-800";
      if (s >= 0.7) return "bg-yellow-100 text-yellow-800";
      return "bg-red-100 text-red-800";
    };


  return (
    <div className="fixed inset-0 flex bg-white z-50">
      <WorkistSidebar />

      <div className="flex flex-1 flex-col">
        <PDFTopbar filename={`${email.id}.pdf`} onClose={onClose} />


        <div className="flex flex-1 overflow-hidden">
          {/* PDF Viewer */}
          <iframe
            title="PDF Viewer"
            src={`data:application/pdf;base64,${email.pdf_attachment}#view=fitH`}
            className="flex-1 bg-black"
          />

          {/* Side Panel */}
          <div className="w-[400px] p-4 border-l bg-gray-50 overflow-y-auto space-y-6">
            {/* Header Data */}
            {/* Header Data */}
              <details open className="bg-white rounded shadow">
  <summary className="flex items-center justify-between px-4 py-3 cursor-pointer bg-gray-100 border-b">
    <span className="font-semibold text-sm">Header data</span>
    <button
      onClick={(e) => {
        e.preventDefault();
        setEditHeader(!editHeader);
      }}
    >
      <Pencil size={16} className="text-gray-500 hover:text-gray-800" />
    </button>
  </summary>

  <div className="p-4 space-y-3 text-sm">
    {Object.entries(email.response || {})
      .filter(([k]) => k !== "Positionen")
      .map(([key, value]) => {
        const s =
          typeof email.confidence?.[key] === "number"
            ? (email.confidence?.[key] as number)
            : undefined;

        return (
          <label key={key} className="block">
            <div className="flex items-center justify-between">
              <span className="text-gray-700">{key}:</span>
              <span className={`text-[11px] px-2 py-0.5 rounded ${scoreColor(s)}`}>
                {fmtScore(s)}
              </span>
            </div>
            {typeof value === "string" && value.length > 60 ? (
              <textarea
                disabled={!editHeader}
                defaultValue={value as string}
                className={`w-full border px-2 py-1 rounded mt-1 ${
                  editHeader ? "bg-yellow-100" : "bg-white"
                }`}
              />
            ) : (
              <input
                disabled={!editHeader}
                defaultValue={value as any}
                className={`w-full border px-2 py-1 rounded mt-1 ${
                  editHeader ? "bg-yellow-100" : "bg-white"
                }`}
              />
            )}
          </label>
        );
      })}
  </div>
</details>


{/* Positionen */}
              <details open className="bg-white rounded shadow">
  <summary className="flex items-center justify-between px-4 py-3 cursor-pointer bg-gray-100 border-b">
    <span className="font-semibold text-sm">Positionen</span>
  </summary>

  <div className="p-4 space-y-4 text-sm">
    {(email.response?.Positionen || []).map((pos, idx) => {
      const isEditing = editPosition === idx;
      const posScore =
        Array.isArray(email.confidence?.Positionen)
          ? (email.confidence?.Positionen as any[])[idx]
          : undefined; // z.B. { Position:0.99, Artikelnummer:0.98, ... }

      return (
        <div key={idx} className="space-y-3 border p-3 rounded relative">
          <button
            onClick={() => setEditPosition(isEditing ? null : idx)}
            className="absolute top-2 right-2 text-gray-500 hover:text-gray-800"
          >
            <Pencil size={16} />
          </button>

          {Object.entries(pos).map(([k, v]) => {
            const s =
              posScore && typeof posScore[k] === "number"
                ? (posScore[k] as number)
                : undefined;

            const isLong = typeof v === "string" && (v as string).length > 60;

            return (
              <label key={k} className="block">
                <div className="flex items-center justify-between">
                  <span className="text-gray-700">{k}:</span>
                  <span className={`text-[11px] px-2 py-0.5 rounded ${scoreColor(s)}`}>
                    {fmtScore(s)}
                  </span>
                </div>

                {isLong ? (
                  <textarea
                    disabled={!isEditing}
                    defaultValue={v as any}
                    className={`w-full border px-2 py-1 rounded mt-1 ${
                      isEditing ? "bg-yellow-100" : "bg-white"
                    }`}
                  />
                ) : (
                  <input
                    disabled={!isEditing}
                    defaultValue={v as any}
                    className={`w-full border px-2 py-1 rounded mt-1 ${
                      isEditing ? "bg-yellow-100" : "bg-white"
                    }`}
                  />
                )}
              </label>
            );
          })}
        </div>
      );
    })}
  </div>
</details>



            {/* Footer Action */}
            <button className="w-full bg-green-600 text-white rounded-full py-2 hover:bg-green-700">
              Close and go to the next task
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
