import React from "react";

function StepOne({ nextStep, handleChange }) {
  return (
    <div>
      <h2>Select Category</h2>

      <select onChange={handleChange("category")}>
        <option value="">Choose...</option>
        <option value="health">Health</option>
        <option value="education">Education</option>
      </select>

      <button onClick={nextStep}>Next</button>
    </div>
  );
}

export default StepOne;
