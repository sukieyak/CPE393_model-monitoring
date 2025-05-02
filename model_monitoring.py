import pandas as pd
import numpy as np
from evidently import Report, Dataset, DataDefinition, Regression
from evidently.metrics import (
    MeanError, MAE, MAPE, RMSE, R2Score, AbsMaxError,
    DummyMAE, DummyMAPE, DummyRMSE
)
from evidently.presets import DataDriftPreset

# Load dataset
flight_data = pd.read_csv('DelayedFlights.csv')  # Adjust the path if needed

# Select features and target variable
features_list = ['DepTime', 'Distance', 'AirTime']  # Adjust based on dataset
target_variable = 'ArrDelay'

# Preprocess the dataset (remove missing values)
flight_data_clean = flight_data[features_list + [target_variable]].dropna()

# Simulate predictions (introduce noise for model predictions)
flight_data_clean['predicted_delay'] = flight_data_clean[target_variable] + np.random.normal(0, 10, flight_data_clean.shape[0])

# Create reference and current datasets
reference_sample = flight_data_clean.sample(n=5000, random_state=42)
current_sample = flight_data_clean.sample(n=5000, random_state=43)

# Define data structure for EvidentlyAI
data_structure = DataDefinition(
    regression=[Regression(target=target_variable, prediction="predicted_delay")]
)

# Convert the data into EvidentlyAI dataset format
reference_evidently_data = Dataset.from_pandas(pd.DataFrame(reference_sample), data_definition=data_structure)
current_evidently_data = Dataset.from_pandas(pd.DataFrame(current_sample), data_definition=data_structure)

# Define model quality metrics and features to enhance the report
quality_report = Report([
    MeanError(),
    MAE(),
    MAPE(),
    RMSE(),
    R2Score(),
    AbsMaxError(),
    DummyMAE(),
    DummyMAPE(),
    DummyRMSE(),
])

# Generate the model quality report
quality_snapshot = quality_report.run(current_evidently_data, reference_evidently_data)

# Save the quality report with a custom file name and style
quality_snapshot.save_html("model_quality.html")

# Optional: Create a data drift report to monitor distribution shifts
drift_analysis_report = Report([DataDriftPreset(method="psi")], include_tests=True)
drift_results = drift_analysis_report.run(reference_sample, current_sample)

# Save the data drift report with a custom file name
drift_results.save_html("report.html")

print("Enhanced model quality and data drift reports have been generated successfully!")
