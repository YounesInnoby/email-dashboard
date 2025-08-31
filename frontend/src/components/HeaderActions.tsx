// components/HeaderActions.tsx
import { BiDotsVerticalRounded } from "react-icons/bi";

export default function HeaderActions() {
  return (
    <div className="flex items-center space-x-4">
      <button className="bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm px-3 py-1 rounded">
        Send file …
      </button>
      <button className="text-gray-600 hover:bg-gray-100 p-2 rounded">
        <BiDotsVerticalRounded size={20} />
      </button>
    </div>
  );
}
