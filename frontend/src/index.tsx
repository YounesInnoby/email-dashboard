import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

// Basename = PUBLIC_URL (bei CRA aus package.json -> "homepage": "/app")
const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  //<React.StrictMode>
  <BrowserRouter basename={process.env.PUBLIC_URL}>
    <App />
  </BrowserRouter>
  //</React.StrictMode>
);

reportWebVitals();
