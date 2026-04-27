import React from "react";

function OutputCard({ output, onBack, onRestart }) {

  const cardStyle = {
    background: "#FFFFFF",
    borderRadius: "10px",
    padding: "20px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
    marginBottom: "20px"
  };

  const sectionTitle = {
    fontSize: "13px",
    fontWeight: "600",
    color: "#0D9488",
    marginBottom: "14px",
    textTransform: "uppercase",
    letterSpacing: "0.5px"
  };

  const getBadge = (status) => {
    const base = {
      padding: "6px 10px",
      borderRadius: "6px",
      fontSize: "12px",
      fontWeight: "500"
    };

    if (status === "success") {
      return <span style={{ ...base, background: "#DCFCE7", color: "#166534" }}>✓ Success</span>;
    }
    if (status === "pending") {
      return <span style={{ ...base, background: "#FEF9C3", color: "#854D0E" }}>⏳ Pending</span>;
    }
    if (status === "error") {
      return <span style={{ ...base, background: "#FEE2E2", color: "#991B1B" }}>✗ Error</span>;
    }
    return null;
  };

  return (
    <div style={{ maxWidth: "800px" }}>

      {/* HEADER */}
      <h1 style={{ color: "#0F172A", marginBottom: "6px" }}>
        Your Results 📋
      </h1>
      <p style={{ color: "#64748B", marginBottom: "20px" }}>
        Here is what our system found for you
      </p>

      {/* INSIGHT */}
      <div style={{ ...cardStyle, borderLeft: "4px solid #0D9488" }}>
        <div style={{
          display: "flex",
          justifyContent: "space-between",
          gap: "12px"
        }}>
          <div style={{
            fontSize: "18px",
            fontWeight: "600",
            color: "#0F172A",
            lineHeight: "1.5"
          }}>
            {output.insight}
          </div>
          {getBadge(output.status)}
        </div>
      </div>

      {/* SUGGESTIONS */}
      {output.suggestions?.length > 0 && (
        <div style={cardStyle}>
          <div style={sectionTitle}>💡 Suggestions</div>

          {output.suggestions.map((s, i) => (
            <div key={i} style={{
              display: "flex",
              gap: "12px",
              marginBottom: "12px"
            }}>
              <div style={{
                minWidth: "26px",
                height: "26px",
                borderRadius: "50%",
                background: "#0D9488",
                color: "#fff",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: "12px",
                fontWeight: "600"
              }}>
                {i + 1}
              </div>

              <div style={{
                fontSize: "14px",
                color: "#475569",
                lineHeight: "1.5"
              }}>
                {s}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* JOBS */}
      {output.jobs?.length > 0 && (
        <div style={cardStyle}>
          <div style={sectionTitle}>🎯 Matching Opportunities</div>

          {output.jobs.map((job, i) => (
            <div key={i} style={{
              display: "flex",
              alignItems: "center",
              gap: "10px",
              padding: "10px",
              background: "#F1F5F9",
              borderRadius: "6px",
              marginBottom: "8px"
            }}>
              <div style={{
                background: "#0D9488",
                color: "#fff",
                borderRadius: "50%",
                width: "24px",
                height: "24px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: "12px",
                fontWeight: "600"
              }}>
                {i + 1}
              </div>

              <span style={{ color: "#0F172A" }}>{job}</span>
            </div>
          ))}
        </div>
      )}

      {/* ACTIONS */}
      {output.actions?.length > 0 && (
        <div style={cardStyle}>
          <div style={sectionTitle}>⚡ Actions</div>

          <div style={{ display: "flex", gap: "12px", flexWrap: "wrap" }}>
            {output.actions.map((action, i) => (
              <button
                key={i}
                onClick={() => {
                  if (action === "Apply Now") {
                    alert("Application process started successfully!");
                  } else {
                    alert(`Action: ${action}`);
                  }
                }}
                style={{
                  background: i === 0 ? "#0D9488" : "transparent",
                  color: i === 0 ? "#fff" : "#0D9488",
                  border: "1px solid #0D9488",
                  padding: "10px 16px",
                  borderRadius: "6px",
                  cursor: "pointer"
                }}
              >
                {action}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* NAVIGATION */}
      <div style={{ display: "flex", gap: "12px" }}>
        <button
          onClick={onBack}
          style={{
            border: "1px solid #0D9488",
            background: "transparent",
            color: "#0D9488",
            padding: "10px 16px",
            borderRadius: "6px"
          }}
        >
          ← Try Again
        </button>

        <button
          onClick={onRestart}
          style={{
            background: "#0D9488",
            color: "#fff",
            border: "none",
            padding: "10px 16px",
            borderRadius: "6px"
          }}
        >
          🔄 Start Over
        </button>
      </div>

    </div>
  );
}

export default OutputCard;