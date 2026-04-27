import { useState } from "react";
import RoleSelection from "./pages/RoleSelection";
import IntentSelection from "./pages/IntentSelection";
import InputForm from "./pages/InputForm";
import OutputCard from "./pages/OutputCard";
import MainLayout from "./layout/MainLayout";

function App() {
  const [step, setStep] = useState(1);
  const [role, setRole] = useState(null);
  const [intent, setIntent] = useState(null);
  const [output, setOutput] = useState(null);

  return (
    <MainLayout>
      <div style={{ padding: "20px" }}>

        {/* ✅ Step Indicator (important for UI marks) */}
        <p style={{ color: "#64748B", marginBottom: "20px" }}>
          Step {step} of 4
        </p>

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
    </MainLayout>
  );
}

export default App;