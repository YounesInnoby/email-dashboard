// src/components/PdfDetailPanel.tsx
import React from "react";
import { FiChevronLeft, FiChevronRight, FiDownload } from "react-icons/fi";
import type { EmailWithResponse } from "../types";

type Props = {
  email: EmailWithResponse;
  onClose: () => void;
};

export default function PdfDetailPanel({ email, onClose }: Props) {
  const { pdf_attachment, response } = email;

  return (
    <div className="flex flex-col h-full">
      {/* Tabs */}
      <div className="flex items-center border-b bg-gray-100 px-6">
        <span className="px-4 py-3 text-sm text-gray-500">Origin Data</span>
        <span className="px-4 py-3 border-b-2 border-blue-600 font-semibold text-sm text-blue-600">
          Document
        </span>
      </div>

      <div className="flex flex-1 overflow-hidden">
        {/* PDF & Controls */}
        <div className="relative flex-1">
          <iframe
            title="PDF Viewer"
            src={`data:application/pdf;base64,${pdf_attachment}#view=fitH`}
            className="w-full h-full"
          />
          <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-white bg-opacity-80 rounded-full flex space-x-3 px-4 py-2 shadow-md hover:bg-opacity-100 transition">
            <button><FiChevronLeft size={20} /></button>
            <button><FiChevronRight size={20} /></button>
            <button><FiDownload size={20} /></button>
          </div>
        </div>

        {/* Metadata & Actions Side */}
        <div className="w-[360px] bg-gray-100 p-6 flex flex-col">
          {/* Header data */}
          <details open className="mb-4 bg-white rounded shadow">
            <summary className="flex justify-between items-center px-4 py-2 cursor-pointer font-semibold text-gray-700 bg-gray-50">
              Header data
              <span className="text-green-600 font-semibold">Completed</span>
            </summary>
            <div className="px-4 py-2 text-sm">
              {Object.entries(response ?? {}).map(([k, v]) =>
                k !== "Positionen" ? (
                  <div key={k} className="flex justify-between mb-2">
                    <span className="text-gray-600">{k}</span>
                    <span className="text-gray-800">{v as string}</span>
                  </div>
                ) : null
              )}
            </div>
          </details>

          {/* Items */}
          <details open className="mb-6 bg-white rounded shadow">
            <summary className="flex justify-between items-center px-4 py-2 cursor-pointer font-semibold text-gray-700 bg-gray-50">
              Items
              <span className="text-green-600 font-semibold">Completed</span>
            </summary>
            <div className="px-4 py-2 text-sm space-y-2">
              {(response?.Positionen || []).map((pos, i) => (
                <div key={i} className="border rounded p-2 bg-gray-50">
                  {Object.entries(pos).map(([k, v]) => (
                    <div key={k} className="flex justify-between">
                      <span className="text-gray-600">{k}</span>
                      <span className="text-gray-800">{v as any}</span>
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </details>

          <button
            onClick={onClose}
            className="mt-auto bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-full font-medium text-sm"
          >
            Close and go to the next task
          </button>
        </div>
      </div>
    </div>
  );
}
