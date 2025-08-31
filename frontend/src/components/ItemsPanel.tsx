import { EmailWithResponse } from "../types";

export default function ItemsPanel({ email }: { email: EmailWithResponse }) {
  const items = email.response?.Positionen ?? [];

  return (
    <div className="mt-2 space-y-3">
      {items.map((item, idx) => (
        <div key={idx} className="border p-3 bg-gray-50 rounded">
          <h4 className="text-sm font-semibold mb-2">Position {item.Position}</h4>
          {Object.entries(item).map(([key, val]) => (
            <div key={key}>
              <label className="text-sm text-gray-600">{key}</label>
              <input
                value={val as any}
                className="w-full border rounded p-1 bg-white mb-2"
                readOnly
              />
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}
