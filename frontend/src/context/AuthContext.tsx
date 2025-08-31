import { createContext, useContext, useMemo, useState, useEffect, ReactNode } from "react";

type AuthState = {
  role: string | null;
  token: string | null;
  setRole: (r: string | null) => void;
  setToken: (t: string | null) => void;
  logout: () => void;
  isAuthenticated: boolean;
};

const AuthContext = createContext<AuthState | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [role, setRole] = useState<string | null>(localStorage.getItem("role"));
  const [token, setToken] = useState<string | null>(localStorage.getItem("token"));

  useEffect(() => {
    role ? localStorage.setItem("role", role) : localStorage.removeItem("role");
  }, [role]);
  useEffect(() => {
    token ? localStorage.setItem("token", token) : localStorage.removeItem("token");
  }, [token]);

  const logout = () => {
    setRole(null);
    setToken(null);
  };

  const value = useMemo(
    () => ({ role, token, setRole, setToken, logout, isAuthenticated: !!token }),
    [role, token]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
