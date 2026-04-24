import React, { useState } from 'react';
import RoleSelection from './pages/RoleSelection';
import IntentSelection from './pages/IntentSelection';
import InputForm from './pages/InputForm';
import OutputCard from './pages/OutputCard';
import './App.css';

function App() {
  const [currentScreen, setCurrentScreen] = useState('role');
  const [selectedRole, setSelectedRole] = useState(null);
  const [selectedIntent, setSelectedIntent] = useState(null);
  const [output, setOutput] = useState(null);

  const handleRoleSelect = (role) => {
    setSelectedRole(role);
    setCurrentScreen('intent');
  };

  const handleIntentSelect = (intent) => {
    setSelectedIntent(intent);
    setCurrentScreen('form');
  };

  const handleFormSubmit = (result) => {
    setOutput(result);
    setCurrentScreen('output');
  };

  const handleBack = () => {
    if (currentScreen === 'intent') setCurrentScreen('role');
    else if (currentScreen === 'form') setCurrentScreen('intent');
    else if (currentScreen === 'output') setCurrentScreen('form');
  };

  const handleRestart = () => {
    setCurrentScreen('role');
    setSelectedRole(null);
    setSelectedIntent(null);
    setOutput(null);
  };

  return (
    <div className="app">
      <nav className="navbar">
        <div className="nav-brand">🤖 Platform Copilot</div>
        {currentScreen !== 'role' && (
          <div className="nav-steps">
            <span className={currentScreen === 'intent' ? 'step active' : 'step done'}>1. Role</span>
            <span className="step-arrow">→</span>
            <span className={currentScreen === 'form' ? 'step active' : currentScreen === 'output' ? 'step done' : 'step'}>2. Intent</span>
            <span className="step-arrow">→</span>
            <span className={currentScreen === 'output' ? 'step active' : 'step'}>3. Result</span>
          </div>
        )}
        {currentScreen !== 'role' && (
          <button className="btn-secondary" onClick={handleRestart}>Start Over</button>
        )}
      </nav>
      <div className="main-content">
        {currentScreen === 'role' && (
          <RoleSelection onRoleSelect={handleRoleSelect} />
        )}
        {currentScreen === 'intent' && (
          <IntentSelection
            role={selectedRole}
            onIntentSelect={handleIntentSelect}
            onBack={handleBack}
          />
        )}
        {currentScreen === 'form' && (
          <InputForm
            role={selectedRole}
            intent={selectedIntent}
            onSubmit={handleFormSubmit}
            onBack={handleBack}
          />
        )}
        {currentScreen === 'output' && (
          <OutputCard
            output={output}
            onBack={handleBack}
            onRestart={handleRestart}
          />
        )}
      </div>
    </div>
  );
}

export default App;