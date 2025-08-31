import React from "react";
import {
  Search,
  Filter,
  SortAsc,
  Inbox,
  CheckCircle,
  Clock,
  AlertTriangle,
} from "lucide-react";

export type StatusTab = "inbox" | "bearbeitet" | "in_bearbeitung" | "action_required";

interface TopBarProps {
  activeTab: StatusTab;
  onChange: (tab: StatusTab) => void;
  // Optional: Counts für Badges (kannst du weglassen, wenn nicht gebraucht)
  counts?: Partial<Record<StatusTab, number>>;
}

export default function TopBar({ activeTab, onChange, counts }: TopBarProps) {
  const TABS: { key: StatusTab; label: string; Icon: React.ComponentType<any> }[] = [
    { key: "inbox",           label: "Inbox",           Icon: Inbox },
    { key: "bearbeitet",      label: "Bearbeitet",      Icon: CheckCircle },
    { key: "in_bearbeitung",  label: "In Bearbeitung",  Icon: Clock },
    { key: "action_required", label: "Action Required", Icon: AlertTriangle },
  ];

  return (
    <div className="flex justify-between items-center bg-white border-b px-6 py-3">
      {/* Links: Tabs */}
      <div className="flex items-center space-x-6">
        {TABS.map(({ key, label, Icon }) => {
          const selected = activeTab === key;
          const badge = counts?.[key];
          return (
            <button
              key={key}
              onClick={() => onChange(key)}
              className={`flex items-center space-x-2 pb-2 border-b-2 transition
                ${selected ? "border-blue-600 text-blue-600 font-medium" :
                  "border-transparent text-gray-500 hover:text-gray-700"}`}
              aria-pressed={selected}
            >
              <Icon className="w-4 h-4" />
              <span>{label}</span>
              {typeof badge === "number" && (
                <span className="ml-1 text-[10px] px-1.5 py-0.5 rounded bg-gray-200">
                  {badge}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Rechts: Search / Filter / Order */}
      <div className="flex items-center space-x-4">
        <button className="text-sm text-gray-600 flex items-center space-x-1 hover:text-gray-800">
          <Search className="w-4 h-4" />
          <span>Search</span>
        </button>
        <button className="text-sm text-gray-600 flex items-center space-x-1 hover:text-gray-800">
          <Filter className="w-4 h-4" />
          <span>Filters</span>
        </button>
        <button className="text-sm text-gray-600 flex items-center space-x-1 hover:text-gray-800">
          <SortAsc className="w-4 h-4" />
          <span>Order by</span>
        </button>
      </div>
    </div>
  );
}
