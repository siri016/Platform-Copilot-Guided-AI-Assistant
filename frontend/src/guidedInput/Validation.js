export const validateInput = (data) => {
  if (!data.category) {
    return "Category is required";
  }
  if (!data.query || data.query.length < 5) {
    return "Query must be at least 5 characters";
  }
  return null;
};
