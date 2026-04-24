import React from 'react';

function OutputCard({ output, onBack, onRestart }) {

  const getBadge = (status) => {
    if (status === 'success') return <span className="badge-success">✓ Success</span>;
    if (status === 'pending') return <span className="badge-pending">⏳ Pending</span>;
    if (status === 'error')   return <span className="badge-error">✗ Error</span>;
    return null;
  };

  return (
    <div style={{ maxWidth: '700px' }}>

      <div className="page-title">Your Results 📋</div>
      <div className="page-sub">
        Here is what our system found for you
      </div>

      {/* Main Insight Card */}
      <div className="card" style={{
        borderLeft: '4px solid #0D9488',
        marginBottom: '20px'
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          gap: '12px'
        }}>
          <div style={{
            fontSize: '18px',
            fontWeight: 'bold',
            color: '#0F172A',
            flex: 1,
            lineHeight: '1.5'
          }}>
            {output.insight}
          </div>
          {getBadge(output.status)}
        </div>
      </div>

      {/* Suggestions Card */}
      {output.suggestions && output.suggestions.length > 0 && (
        <div className="card" style={{ marginBottom: '20px' }}>
          <div style={{
            fontSize: '13px',
            fontWeight: 'bold',
            color: '#0D9488',
            marginBottom: '16px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            💡 Suggestions
          </div>

          {output.suggestions.map((s, i) => (
            <div key={i} style={{
              display: 'flex',
              gap: '12px',
              marginBottom: '12px',
              alignItems: 'flex-start'
            }}>
              <div style={{
                minWidth: '26px',
                height: '26px',
                borderRadius: '50%',
                background: '#0D9488',
                color: '#fff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '12px',
                fontWeight: 'bold',
                flexShrink: 0
              }}>
                {i + 1}
              </div>
              <div style={{
                fontSize: '14px',
                color: '#475569',
                paddingTop: '4px',
                lineHeight: '1.5'
              }}>
                {s}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Candidates List — HR only */}
      {output.candidates && output.candidates.length > 0 && (
        <div className="card" style={{ marginBottom: '20px' }}>
          <div style={{
            fontSize: '13px',
            fontWeight: 'bold',
            color: '#0D9488',
            marginBottom: '16px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            👥 Candidates
          </div>

          {output.candidates.map((c, i) => (
            <div key={i} style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              padding: '10px 14px',
              background: '#F1F5F9',
              borderRadius: '6px',
              marginBottom: '8px'
            }}>
              <span style={{
                fontWeight: '500',
                color: '#0F172A'
              }}>
                {c.name}
              </span>
              <span style={{
                color: '#0D9488',
                fontWeight: '500'
              }}>
                {c.score}
              </span>
              <span className="badge-pending">{c.status}</span>
            </div>
          ))}
        </div>
      )}

      {/* Jobs List — Student only */}
      {output.jobs && output.jobs.length > 0 && (
        <div className="card" style={{ marginBottom: '20px' }}>
          <div style={{
            fontSize: '13px',
            fontWeight: 'bold',
            color: '#0D9488',
            marginBottom: '16px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            🎯 Matching Opportunities
          </div>

          {output.jobs.map((job, i) => (
            <div key={i} style={{
              padding: '10px 14px',
              background: '#F1F5F9',
              borderRadius: '6px',
              marginBottom: '8px',
              fontSize: '14px',
              color: '#0F172A',
              display: 'flex',
              gap: '10px',
              alignItems: 'center'
            }}>
              <span style={{
                background: '#0D9488',
                color: '#fff',
                borderRadius: '50%',
                width: '24px',
                height: '24px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '12px',
                fontWeight: 'bold',
                flexShrink: 0
              }}>
                {i + 1}
              </span>
              {job}
            </div>
          ))}
        </div>
      )}

      {/* Referral History — Referrer only */}
      {output.history && output.history.length > 0 && (
        <div className="card" style={{ marginBottom: '20px' }}>
          <div style={{
            fontSize: '13px',
            fontWeight: 'bold',
            color: '#0D9488',
            marginBottom: '16px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            📋 Referral History
          </div>

          {output.history.map((item, i) => (
            <div key={i} style={{
              padding: '10px 14px',
              background: '#F1F5F9',
              borderRadius: '6px',
              marginBottom: '8px',
              fontSize: '14px',
              color: '#0F172A'
            }}>
              {i + 1}. {item}
            </div>
          ))}
        </div>
      )}

      {/* Action Buttons */}
      {output.actions && output.actions.length > 0 && (
        <div className="card" style={{ marginBottom: '20px' }}>
          <div style={{
            fontSize: '13px',
            fontWeight: 'bold',
            color: '#0D9488',
            marginBottom: '16px',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}>
            ⚡ Actions
          </div>

          <div style={{
            display: 'flex',
            gap: '12px',
            flexWrap: 'wrap'
          }}>
            {output.actions.map((action, i) => (
              <button
                key={i}
                className={i === 0 ? 'btn-primary' : 'btn-secondary'}
                onClick={() => alert(`Action: ${action}`)}
              >
                {action}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Navigation Buttons */}
      <div style={{
        display: 'flex',
        gap: '12px',
        marginTop: '8px'
      }}>
        <button className="btn-secondary" onClick={onBack}>
          ← Try Again
        </button>
        <button className="btn-primary" onClick={onRestart}>
          🔄 Start Over
        </button>
      </div>

    </div>
  );
}

export default OutputCard;