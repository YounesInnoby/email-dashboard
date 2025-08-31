import { EmailWithResponse } from "../types";

export default function HeaderDataPanel({ email }: { email: EmailWithResponse }) {
  const header = { ...(email.response ?? {}) };
  delete header.Positionen;

  return (
    <div className="mt-2 space-y-2 bg-gray-100 p-3 rounded">
      {Object.entries(header).map(([key, val]) => (
        <div key={key}>
          <label className="block text-sm font-medium text-gray-700">{key}</label>
          <input
            className="w-full border rounded p-1 bg-white"
            value={val as any}
            readOnly
          />
        </div>
      ))}
    </div>
  );
}
