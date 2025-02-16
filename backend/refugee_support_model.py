import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
import json

# Define the five priority areas
PRIORITY_AREAS = [
    "Legal Assistance",
    "Employment & Credential Recognition",
    "Housing Stability",
    "Healthcare & Mental Health Support",
    "Language & Community Integration"
]

# Load dataset
with open("backend/refugee_support_data_weighted.json", "r") as f:
    data = json.load(f)

# Prepare dataset
X = np.array([entry["survey_responses"] for entry in data])
y_labels = [entry["priority_areas"] for entry in data]

# Convert labels to binary format using MultiLabelBinarizer
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(y_labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model with multi-label classification
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Prediction function
def predict_priority_areas(user_input):
    """Takes in a list of 10 numerical responses and returns the top 3 priority areas."""
    user_input = np.array(user_input).reshape(1, -1)
    prediction = rf_model.predict(user_input)[0]
    top_indices = np.argsort(prediction)[-3:][::-1]  # Get top 3 priority indices
    predicted_areas = [PRIORITY_AREAS[i] for i in top_indices]
    return predicted_areas


