import React from "react";

const roles = [
  {
    id: "student",
    label: "Student",
    icon: "🎓",
    desc: "Check application status, find internship opportunities, get profile tips",
    color: "#0D9488",
  },
  {
    id: "hr",
    label: "HR",
    icon: "💼",
    desc: "View candidates, schedule interviews, post new job openings",
    color: "#185FA5",
  },
  {
    id: "referrer",
    label: "Referrer",
    icon: "🤝",
    desc: "Refer candidates, track referral status, view referral history",
    color: "#7C3AED",
  },
  {
    id: "college",
    label: "College",
    icon: "🏫",
    desc: "View placement stats, upload student data, contact HR companies",
    color: "#065F46",
  },
];

function RoleSelection({ onRoleSelect }) {
  return (
    <div>
      {/* Title */}
      <h1
        style={{
          fontSize: "24px",
          fontWeight: "600",
          color: "#0F172A",
          marginBottom: "6px",
        }}
      >
        Welcome to Platform Copilot 👋
      </h1>

      {/* Subtitle */}
      <p style={{ color: "#64748B", marginBottom: "20px" }}>
        Select your role to continue
      </p>

      {/* Role Grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
          gap: "20px",
        }}
      >
        {roles.map((role) => (
          <div
            key={role.id}
            onClick={() => onRoleSelect(role)}
            style={{
              background: "#FFFFFF",
              borderRadius: "10px",
              padding: "20px",
              cursor: "pointer",
              border: "1px solid #E2E8F0",
              boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
              transition: "all 0.2s ease",
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = "translateY(-3px)";
              e.currentTarget.style.boxShadow =
                "0 6px 16px rgba(0,0,0,0.08)";
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = "translateY(0px)";
              e.currentTarget.style.boxShadow =
                "0 2px 8px rgba(0,0,0,0.06)";
            }}
          >
            {/* Icon */}
            <div
              style={{
                fontSize: "28px",
                marginBottom: "10px",
              }}
            >
              {role.icon}
            </div>

            {/* Title */}
            <div
              style={{
                fontSize: "16px",
                fontWeight: "600",
                color: "#0F172A",
                marginBottom: "6px",
              }}
            >
              {role.label}
            </div>

            {/* Description */}
            <div
              style={{
                fontSize: "13px",
                color: "#475569",
                lineHeight: "1.5",
              }}
            >
              {role.desc}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RoleSelection;