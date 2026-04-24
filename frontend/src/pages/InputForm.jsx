import React, { useState } from 'react';
import axios from 'axios';

function InputForm({ role, intent, onSubmit, onBack }) {
  const [inputs, setInputs] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (fieldId, value) => {
    setInputs(prev => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = async () => {
    // Validate all fields are filled
    for (let field of intent.fields) {
      if (!inputs[field.id] || inputs[field.id] === '') {
        setError(`Please fill in: ${field.label}`);
        return;
      }
    }

    setLoading(true);
    setError('');

    try {
      const res = await axios.post('http://127.0.0.1:5000/api/process', {
        role: role.id,
        intent: intent.id,
        inputs: inputs
      });
      onSubmit(res.data);
    } catch (err) {
      setError('Something went wrong. Please make sure Flask is running!');
    }

    setLoading(false);
  };

  return (
    <div>
      {/* Header */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '14px',
        marginBottom: '8px'
      }}>
        <div style={{
          width: '48px',
          height: '48px',
          borderRadius: '50%',
          background: '#0D9488',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '22px'
        }}>
          {role.icon}
        </div>
        <div>
          <div className="page-title" style={{ marginBottom: 0 }}>
            {intent.label}
          </div>
          <div style={{ fontSize: '13px', color: '#475569', marginTop: '2px' }}>
            Step 3 of 3 — Fill in the details below
          </div>
        </div>
      </div>

      <div className="page-sub" style={{ marginTop: '16px' }}>
        All fields are required — no fre