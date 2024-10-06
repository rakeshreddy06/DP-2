# Differential Privacy Implementation

This project demonstrates the Laplace and Exponential Mechanisms for differential privacy using an adult dataset.

## Laplace Mechanism

- **Global Sensitivity**: Calculated as `(max age - min age) / record count` for ages above 25.
- **Steps**:
  1. Compute average age for ages > 25.
  2. Determine global sensitivity.
  3. Calculate variance using sensitivity and epsilon.
  4. Add Laplace noise to the average age.
  5. Output the noise-added result.

Higher epsilon values yield more accurate results; lower values increase privacy.

## Exponential Mechanism

- **Global Sensitivity**: 1, as adding/removing a record changes one education level.
- **Steps**:
  1. Calculate utility scores for education levels.
  2. Use a scaling factor for large counts.
  3. Compute probabilities with epsilon and sensitivity.
  4. Output based on probabilities.

Lower epsilon values increase privacy, altering the most frequent education output.

## Conclusion

This project illustrates the balance between privacy and accuracy in differential privacy.
