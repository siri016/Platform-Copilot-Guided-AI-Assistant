import React from "react";

export default function MainLayout({ children }) {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      
      {/* Sidebar */}
      <div style={{
        width: "220px",
        background: "#0F172A",
        color: "white",
        padding: "20px"
      }}>
        <h2 style={{ color: "#0D9488" }}>Copilot</h2>
      </div>

      {/* Main Content */}
      <div style={{
        flex: 1,
        background: "#F1F5F9",
        padding: "30px"
      }}>
        {children}
      </div>

    </div>
  );
}