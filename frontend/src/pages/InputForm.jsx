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
    // Validate all fields
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
      setError('Something went wrong. Make sure Flask backend is running!');
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
          <div style={{ fontSize: '13px', color: '#475569' }}>
            Step 3 of 3 — Fill in the details below
          </div>
        </div>
      </div>

      {/* Form Fields */}
      <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {intent.fields.map((field) => (
          <div key={field.id}>
            <label style={{ fontSize: '14px', fontWeight: '500' }}>
              {field.label}
            </label>

            {/* TEXT INPUT */}
            {field.type === 'text' && (
              <input
                type="text"
                placeholder={field.label}
                style={{ width: '100%', padding: '8px', marginTop: '4px' }}
                onChange={(e) => handleChange(field.id, e.target.value)}
              />
            )}

            {/* SELECT INPUT */}
            {field.type === 'select' && (
              <select
                style={{ width: '100%', padding: '8px', marginTop: '4px' }}
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

      {/* Error */}
      {error && (
        <div style={{ color: 'red', marginTop: '12px' }}>
          {error}
        </div>
      )}

      {/* Buttons */}
      <div style={{
        display: 'flex',
        gap: '12px',
        marginTop: '20px'
      }}>
        <button onClick={onBack}>
          ← Back
        </button>

        <button onClick={handleSubmit} disabled={loading}>
          {loading ? 'Processing...' : 'Submit'}
        </button>
      </div>
    </div>
  );
}

export default InputForm;