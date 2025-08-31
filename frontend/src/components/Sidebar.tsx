// src/components/Sidebar.tsx
import { ClipboardCheck, ShoppingCart, FileText, BarChart2, Settings, LifeBuoy } from "lucide-react";

type TabKey = "client-request" | "order" | "invoice";

type Props = {
  active: TabKey;
  counts: Record<TabKey, number>;
  onChange: (tab: TabKey) => void;
};

export default function Sidebar({ active, counts, onChange }: Props) {
  const btnBase =
    "w-full flex items-center justify-between px-3 py-2 rounded-md text-sm transition";
  const activeCls = "bg-blue-50 text-blue-700";
  const idleCls = "text-gray-700 hover:bg-gray-100";

  return (
    <aside className="w-64 bg-white border-r h-screen flex flex-col">
      {/* Top-Bereich (Logo und Tabs) */}
      <div className="p-4 flex-shrink-0">
        <img src={`${process.env.PUBLIC_URL}/Innoby_claim.png`} alt="Logo" />
      </div>

      <div className="text-xs uppercase tracking-wider text-gray-400 mb-3 px-4">
        Documents
      </div>

      {/* Reiter für Dokumente */}
      <div className="space-y-2 px-4 flex-1">
        <button
          className={`${btnBase} ${active === "client-request" ? activeCls : idleCls}`}
          onClick={() => onChange("client-request")}
        >
          <span className="flex items-center gap-2">
            <ClipboardCheck size={16} />
            <span>Client Request</span>
          </span>
          <span className="text-xs bg-gray-200 px-2 rounded-full">
            {counts["client-request"] ?? 0}
          </span>
        </button>

        <button
          className={`${btnBase} ${active === "order" ? activeCls : idleCls}`}
          onClick={() => onChange("order")}
        >
          <span className="flex items-center gap-2">
            <ShoppingCart size={16} />
            <span>Order</span>
          </span>
          <span className="text-xs bg-gray-200 px-2 rounded-full">
            {counts["order"] ?? 0}
          </span>
        </button>

        <button
          className={`${btnBase} ${active === "invoice" ? activeCls : idleCls}`}
          onClick={() => onChange("invoice")}
        >
          <span className="flex items-center gap-2">
            <FileText size={16} />
            <span>Invoice</span>
          </span>
          <span className="text-xs bg-gray-200 px-2 rounded-full">
            {counts["invoice"] ?? 0}
          </span>
        </button>
      </div>

      {/* BOTTOM-Bereich, fixiert am unteren Rand */}
      <div className="px-4 py-4 border-t space-y-3 text-base text-gray-600 flex-shrink-0">
        <div className="flex items-center gap-2">
          <BarChart2 className="w-4 h-4" />
          <span>Analytics</span>
        </div>
        <div className="flex items-center gap-2">
          <Settings className="w-4 h-4" />
          <span>Settings</span>
        </div>
        <div className="flex items-center gap-2">
          <LifeBuoy className="w-4 h-4" />
          <span>Innoby Support</span>
        </div>
      </div>
    </aside>
  );
}
