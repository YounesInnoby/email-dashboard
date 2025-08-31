import {
  ChevronDown,
  RefreshCcw,
  FileText,
  Sun,
  Database,
  ScanLine,
  ChevronLeft,
  ChevronRight,
  X,
} from "lucide-react";

type Props = {
  filename: string;
  onClose: () => void;
};

export default function PDFTopbar({ filename, onClose }: Props) {
  return (
    <div className="flex items-center h-14 border-b bg-gray-50 text-sm text-gray-700 px-4">
      {/* LEFT: Filename + Status */}
      <div className="flex items-center gap-2 text-base font-medium">
        <span className="w-2 h-2 bg-yellow-500 rounded-full" />
        <span>{filename}</span>
        <ChevronDown className="w-4 h-4" />
      </div>

      {/* Spacer */}
      <div className="flex-grow" />

      {/* RIGHT: Button Cluster */}
      <div className="flex items-center gap-4">
        <button className="flex items-center gap-1 hover:text-black">
          <RefreshCcw size={16} />
          <span>Origin Data</span>
        </button>

        <button className="flex items-center gap-1 bg-green-100 text-green-800 px-2 py-0.5 rounded hover:bg-green-200 text-xs">
          <FileText size={14} />
          <span>Document</span>
        </button>

        <div className="h-6 border-l border-gray-300 mx-2" />

        <button className="text-gray-600 hover:text-black">
          <Sun size={16} />
        </button>
        <button className="text-gray-600 hover:text-black">
          <Database size={16} />
        </button>
        <button className="text-gray-600 hover:text-black">
          <ScanLine size={16} />
        </button>

        <div className="h-6 border-l border-gray-300 mx-2" />

        <div className="flex items-center gap-1 text-xs text-gray-600">
          <ChevronLeft size={16} />
          <span>1 of 1</span>
          <ChevronRight size={16} />
        </div>

        <button onClick={onClose} className="text-gray-600 hover:text-black ml-2">
          <X size={18} />
        </button>
      </div>
    </div>
  );
}
