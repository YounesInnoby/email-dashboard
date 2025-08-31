// src/context/GlobalMenuContext.tsx
import { createContext, useState, useMemo, ReactNode } from "react";

type GlobalMenuApi = {
  visible: boolean;
  setVisible: (v: boolean) => void;
};

export const GlobalMenuContext = createContext<GlobalMenuApi | undefined>(undefined);

export function GlobalMenuProvider({ children }: { children: ReactNode }) {
  const [visible, setVisible] = useState(true);
  const value = useMemo(() => ({ visible, setVisible }), [visible]);
  return <GlobalMenuContext.Provider value={value}>{children}</GlobalMenuContext.Provider>;
}
