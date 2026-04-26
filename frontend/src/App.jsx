import { useState } from "react";
import RoleSelection from "./pages/RoleSelection";
import IntentSelection from "./pages/IntentSelection";
import InputForm from "./pages/InputForm";
import OutputCard from "./pages/OutputCard";

function App() {
  const [step, setStep] = useState(1);
  const [role, setRole] = useState(null);
  const [intent, setIntent] = useState(null);
  const [output, setOutput] = useState(null);

  return (
    <div style={{ padding: "30px" }}>
      {step === 1 && (
        <RoleSelection
          onRoleSelect={(r) => {
            setRole(r);
            setStep(2);
          }}
        />
      )}

      {step === 2 && (
        <IntentSelection
          role={role}
          onIntentSelect={(i) => {
            setIntent(i);
            setStep(3);
          }}
          onBack={() => setStep(1)}
        />
      )}

      {step === 3 && (
        <InputForm
          role={role}
          intent={intent}
          onSubmit={(res) => {
            setOutput(res);
            setStep(4);
          }}
          onBack={() => setStep(2)}
        />
      )}

      {step === 4 && (
        <OutputCard
          output={output}
          onBack={() => setStep(3)}
          onRestart={() => {
            setStep(1);
            setRole(null);
            setIntent(null);
            setOutput(null);
          }}
        />
      )}
    </div>
  );
}

export default App;