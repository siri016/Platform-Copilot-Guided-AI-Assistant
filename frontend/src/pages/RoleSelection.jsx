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
      <div className="page-title">Welcome to Platform Copilot 👋</div>
      <div className="page-su