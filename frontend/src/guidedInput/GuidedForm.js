import React, { useState } from "react";
import StepOne from "./StepOne";
import StepTwo from "./StepTwo";

function GuidedForm() {
  const [step, setStep] = useState(1);
  const [data, setData] = useState({});

  const nextStep = () => setStep(step + 1);
  const prevStep = () => setStep(step - 1);

  const handleChange = (input) => (e) => {
    setData({ ...data, [input]: e.target.value });
  };

  switch (step) {
    case 1:
      return <StepOne nextStep={nextStep} handleChange={handleChange} />;
    case 2:
      return <StepTwo nextStep={nextStep} prevStep={prevStep} handleChange={handleChange} />;
    default:
      return <h2>Done</h2>;
  }
}

export default GuidedForm;
