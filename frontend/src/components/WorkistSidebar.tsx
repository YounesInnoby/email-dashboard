import {
  ShoppingCart,
  DollarSign,
  List,
  BarChart,
  Settings,
  User
} from "lucide-react";

export default function WorkistSidebar() {
  return (
    <div className="w-16 bg-gray-100 flex flex-col justify-between items-center py-4">
      {/* TOP: Logo und Icons */}
      <div className="flex flex-col items-center space-y-6">
        {/* Logo als runder Platzhalter */}
        <div className="w-8 h-8 rounded-full overflow-hidden bg-white">
          <img
            src={`${process.env.PUBLIC_URL}/Innoby_claim.png`}
            alt="Logo"
            className="object-contain w-full h-full"
          />
        </div>



        <DollarSign className="text-gray-700" />

        {/* Aktives Icon hervorgehoben */}
        <div className="relative">
          <div className="absolute -top-1 -right-1 w-2 h-2 bg-orange-500 rounded-full z-10" />
          <div className="bg-teal-100 rounded-md p-1">
            <ShoppingCart className="text-teal-700" />
          </div>
        </div>

        <List className="text-gray-700" />
      </div>

      {/* BOTTOM: Analytics, Settings, Support */}
      <div className="flex flex-col items-center space-y-6">
        <BarChart className="text-gray-700" />
        <Settings className="text-gray-700" />
        <User className="text-gray-700" />
      </div>
    </div>
  );
}
