import { useState, useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { TextField, Button, Box, Typography, Paper, Container, CircularProgress } from "@mui/material";
import { GlobalMenuContext } from "../context/GlobalMenuContext";

const API_BASE =  "http://localhost:8001";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const navigate = useNavigate();
  const globalMenu = useContext(GlobalMenuContext);

  useEffect(() => {
    globalMenu?.setVisible?.(false);
    return () => globalMenu?.setVisible?.(true);
  }, [globalMenu]);

  const handleLogin = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`${API_BASE}/api/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      const data = await res.json();
      if (res.ok) {
        localStorage.setItem("token", data.token ?? "dummy");
        localStorage.setItem("role", data.role ?? "user");
        navigate("/");
      } else {
        setError(data.detail || data.message || "Login fehlgeschlagen");
      }
    } catch {
      setError("Serverfehler. Bitte später erneut versuchen.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Paper elevation={3} sx={{ p: 4, mt: 10, textAlign: "center" }}>
        <img src={`${API_BASE}/Innoby_claim.png`} alt="Logo" />
        <Typography variant="h5" gutterBottom>Login</Typography>
        {error && <Typography color="error">{error}</Typography>}
        <Box sx={{ mt: 2 }}>
          <TextField fullWidth label="Benutzername" margin="normal"
            value={username} onChange={(e) => setUsername(e.target.value)} />
          <TextField fullWidth label="Passwort" type="password" margin="normal"
            value={password} onChange={(e) => setPassword(e.target.value)} />
          <Button fullWidth variant="contained" sx={{ mt: 2 }}
            onClick={handleLogin} disabled={loading}>
            {loading ? <CircularProgress size={24} /> : "Anmelden"}
          </Button>
        </Box>
      </Paper>
    </Container>
  );
}
