import React from 'react';

const roles = [
  {
    id: 'student',
    label: 'Student',
    icon: '🎓',
    desc: 'Check application status, find internship opportunities, get profile tips',
    color: '#0D9488'
  },
  {
    id: 'hr',
    label: 'HR',
    icon: '💼',
    desc: 'View candidates, schedule interviews, post new job openings',
    color: '#185FA5'
  },
  {
    id: 'referrer',
    label: 'Referrer',
    icon: '🤝',
    desc: 'Refer candidates, track referral status, view referral history',
    color: '#7C3AED'
  },
  {
    id: 'college',
    label: 'College',
    icon: '🏫',
    desc: 'View placement stats, upload student data, contact HR companies',
    color: '#065F46'
  },
];

function RoleSelection({ onRoleSelect }) {
  return (
    <div>
      {/* Title */}
      <div className="page-title">Welcome to Platform Copilot 👋</div>

      {/* Subtitle */}
      <div className="page-sub">
        Select your role to continue
      </div>

      {/* Role Cards */}
      <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {roles.map((role) => (
          <div
            key={role.id}
            onClick={() => onRoleSelect(role)}
            style={{
              border: '1px solid #ddd',
              borderRadius: '8px',
              padding: '16px',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '12px'
            }}
          >
            <div style={{ fontSize: '24px' }}>{role.icon}</div>

            <div>
              <div style={{ fontWeight: 'bold' }}>{role.label}</div>
              <div style={{ fontSize: '12px', color: '#555' }}>
                {role.desc}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RoleSelection;