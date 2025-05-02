Findings from Model Quality Report
   Mean Error
      Current: Mean: 9.85, Std: 7.85
      Reference: Mean: 10.06, Std: 8.03
      Interpretation: Mean errors are close (difference of 0.21), showing minimal bias in predictions. Standard deviations align with expected noise, indicating stable error variability.
   Error (Predicted - Actual) Distribution
      Visual Analysis: Errors fluctuate around zero, ranging from -15 to +15, with the mean error line staying near zero.
      Interpretation: Symmetric distribution with no bias, variability aligns with noise (std ~8), and consistency between datasets suggests stable performance.
   Mean Absolute Error (MAE)
      Current: 7.85
      Reference: 8.03
      Interpretation: Predictions deviate by ~8 minutes on average. The small difference (0.18) indicates consistent accuracy across datasets.
   Error Distribution (Histogram)
      Visual Analysis: Errors peak near zero, spreading up to ±40 minutes, with current dataset slightly more concentrated.
      Interpretation: Centered distribution confirms no bias, with most errors within ±20 minutes, matching noise level. Consistency across datasets is evident.
   Mean Absolute Percentage Error (MAPE)
      Current: 43.46%–49.83%
      Reference: 35.24%–39.88%
      Interpretation: Reference model has lower MAPE, suggesting better handling of proportional errors. High values may indicate issues with small actual values.
   Root Mean Squared Error (RMSE)
      Current: 9.85
      Reference: 10.06
      Interpretation: Current model slightly better (difference of 0.21), with errors aligning with noise level, indicating no significant model misfit.
   R² Score
      Current: 0.965
      Reference: 0.968
      Interpretation: Both models explain >96% of variance, with reference slightly better. High scores reflect the simulation design.
   Absolute Max Error
      Current: 36.37
      Reference: 32.77
      Interpretation: Reference model has lower max error (difference of 3.6 minutes), better handling extreme cases.
   Dummy Metrics
      Dummy MAE: 7.85
      Dummy MAPE: Matches actual MAPE range
      Dummy RMSE: 9.85
      Interpretation: Model performance is close to baseline, expected due to noise-based simulation.
   Overall Interpretation
      Model Performance: Minimal bias (mean error ~0), high R² (>0.96), but average error (MAE ~8 minutes) and max error (~36 minutes) suggest room for improvement.
      Error Characteristics: Errors are symmetric, with spread up to ±40 minutes, driven by noise (std ~8). MAPE is high, possibly due to small actual values.
      Comparison to Baseline: Matches dummy metrics, indicating limited improvement over a naive predictor due to simulation.
      Business Implications: 8-minute average error is acceptable for general use, but max errors (~36 minutes) may affect critical decisions.
      Recommendations: Investigate MAPE issues (e.g., small actual values), train a real model to reduce errors, and monitor for drift in production.
   Conclusion
   The model shows stable, unbiased performance with an 8-minute average error and high R², but MAPE issues and baseline-like performance highlight the need for data review and a trained model for better real-world flight delay prediction.