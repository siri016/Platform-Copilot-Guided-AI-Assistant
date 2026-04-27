import React, { useState } from "react";
import axios from "axios";

function InputForm({ role, intent, onSubmit, onBack }) {
  const [inputs, setInputs] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (fieldId, value) => {
    setInputs((prev) => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = async () => {
    for (let field of intent.fields) {
      if (!inputs[field.id] || inputs[field.id] === "") {
        setError(`Please fill in: ${field.label}`);
        return;
      }
    }

    setLoading(true);
    setError("");

    try {
      const res = await axios.post("http://127.0.0.1:5000/api/process", {
        role: role.id,
        intent: intent.id,
        inputs: inputs,
      });

      onSubmit(res.data);
    } catch (err) {
      setError("Something went wrong. Make sure Flask backend is running!");
    }

    setLoading(false);
  };

  const cardStyle = {
    background: "#FFFFFF",
    borderRadius: "10px",
    padding: "24px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
  };

  const inputStyle = {
    width: "100%",
    padding: "10px",
    marginTop: "6px",
    borderRadius: "6px",
    border: "1px solid #CBD5E1",
    outline: "none",
  };

  return (
    <div>
      {/* HEADER */}
      <div style={{ display: "flex", alignItems: "center", gap: "14px", marginBottom: "20px" }}>
        <div
          style={{
            width: "48px",
            height: "48px",
            borderRadius: "50%",
            background: "#0D9488",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: "22px",
            color: "white",
          }}
        >
          {role.icon}
        </div>

        <div>
          <h2 style={{ margin: 0, color: "#0F172A" }}>{intent.label}</h2>
          <p style={{ fontSize: "13px", color: "#64748B" }}>
            Step 3 of 4 — Fill in the details
          </p>
        </div>
      </div>

      {/* FORM CARD */}
      <div style={cardStyle}>
        <div style={{ display: "flex", flexDirection: "column", gap: "18px" }}>
          {intent.fields.map((field) => (
            <div key={field.id}>
              <label
                style={{
                  fontSize: "13px",
                  fontWeight: "600",
                  color: "#0D9488",
                }}
              >
                {field.label}
              </label>

              {/* TEXT INPUT */}
              {field.type === "text" && (
                <input
                  type="text"
                  placeholder={field.label}
                  style={inputStyle}
                  onFocus={(e) => (e.target.style.border = "2px solid #0D9488")}
                  onBlur={(e) => (e.target.style.border = "1px solid #CBD5E1")}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                />
              )}

              {/* SELECT INPUT */}
              {field.type === "select" && (
                <select
                  style={inputStyle}
                  onFocus={(e) => (e.target.style.border = "2px solid #0D9488")}
                  onBlur={(e) => (e.target.style.border = "1px solid #CBD5E1")}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                >
                  <option value="">Select...</option>
                  {field.options.map((opt, i) => (
                    <option key={i} value={opt}>
                      {opt}
                    </option>
                  ))}
                </select>
              )}
            </div>
          ))}
        </div>

        {/* ERROR */}
        {error && (
          <div
            style={{
              marginTop: "16px",
              padding: "10px",
              background: "#FEE2E2",
              color: "#991B1B",
              borderRadius: "6px",
              fontSize: "13px",
            }}
          >
            {error}
          </div>
        )}

        {/* BUTTONS */}
        <div style={{ display: "flex", justifyContent: "space-between", marginTop: "24px" }}>
          <button
            onClick={onBack}
            style={{
              border: "1px solid #0D9488",
              background: "transparent",
              color: "#0D9488",
              padding: "10px 16px",
              borderRadius: "6px",
              cursor: "pointer",
            }}
          >
            ← Back
          </button>

          <button
            onClick={handleSubmit}
            disabled={loading}
            style={{
              background: "#0D9488",
              color: "white",
              border: "none",
              padding: "10px 18px",
              borderRadius: "6px",
              cursor: "pointer",
              opacity: loading ? 0.7 : 1,
            }}
          >
            {loading ? "Processing..." : "Submit"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default InputForm;