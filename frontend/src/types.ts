// src/types.ts
export type Position = Record<string, string | number>;
export type ConfidencePosition = Record<string, number>;

export type Kategorie = "Kundenanfrage" | "Bestellung" | "Rechnung";

export interface EmailWithResponse {
  id: string;
  subject: string;
  sender: string;
  pdf_attachment?: string;
  pdf_text?: string;
  status?: "action_required" | "in_bearbeitung" | "bearbeitet";
  Kategorie: Kategorie; // <— NEU
  response?: {
    [k: string]: any;
    Positionen?: Position[];
  };
  confidence?: {
    [k: string]: number | ConfidencePosition[];
  };
}
