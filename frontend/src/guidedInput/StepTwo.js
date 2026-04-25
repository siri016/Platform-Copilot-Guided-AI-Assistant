import React from "react";

function StepTwo({ nextStep, prevStep, handleChange }) {
  return (
    <div>
      <h2>Enter Details</h2>

      <input
        type="text"
        placeholder="Enter your query"
        onChange={handleChange("query")}
      />

      <br />

      <button onClick={prevStep}>Back</button>
      <button onClick={nextStep}>Submit</button>
    </div>
  );
}

export default StepTwo;
