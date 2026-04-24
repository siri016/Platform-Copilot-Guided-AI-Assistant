import React, { useEffect, useState } from 'react';
import axios from 'axios';

function IntentSelection({ role, onIntentSelect, onBack }) {
  const [intents, setIntents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/intents?role=${role.id}`)
      .then(res => {
        setIntents(res.data.intents);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load intents. Make sure Flask is running!');
        setLoading(false);
      });
  }, [role]);

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
            {role.label} — What do you need help with?
          </div>
          <div style={{ fontSize: '13px', color: '#475569', marginTop: '2px' }}>
            Select one option below to continue
          </div>
        </div>
      </div>

      <div className="page-sub" style={{ marginTop: '16px' }}>
        Step 2 of 3 — Choose your intent
      </div>

      {/* Loading */}
      {loading && (
        <div className="loading">
          Loading options... ⏳
        </div>
      )}

      {/* Error */}
      {error && (
        <div className="error-box">{error}</div>
      )}

      {/* Intent Cards */}
      {!loading && !error && (
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '14px'
        }}>
          {intents.map((intent, i) => (
            <div
              key={intent.id}
              className="card"
              onClick={() => onIntentSelect(intent)}
              style={{
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '16px',
                transition: 'transform 0.2s, box-shadow 0.2s'
              }}
              onMouseEnter={e => {
                e.currentTarget.style.transform = 'translateX(8px)';
                e.currentTarget.style.boxShadow = '0 4px 16px rgba(0,0,0,0.10)';
              }}
              onMouseLeave={e => {
                e.currentTarget.style.transform = 'translateX(0)';
                e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,0.06)';
              }}
            >
              {/* Number */}
              <div style={{
                minWidth: '40px',
                height: '40px',
                borderRadius: '50%',
                background: '#0D9488',
                color: '#fff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '16px',
                fontWeight: 'bold',
                flexShrink: 0
              }}>
                {i + 1}
              </div>

              {/* Label */}
              <div style={{ flex: 1 }}>
                <div style={{
                  fontSize: '16px',
                  fontWeight: '500',
                  color: '#0F172A',
                  marginBottom: '4px'
                }}>
                  {intent.label}
                </div>
                <div style={{ fontSize: '12px', color: '#475569' }}>
                  Click to proceed →
                </div>
              </div>

              {/* Arrow */}
              <div style={{
                color: '#0D9488',
                fontSize: '22px',
                fontWeight: 'bold'
              }}>
                →
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Back Button */}
      <button
        className="btn-secondary"
        onClick={onBack}
        style={{ marginTop: '28px' }}
      >
        ← Back to Role Selection
      </button>
    </div>
  );
}

export default IntentSelection;