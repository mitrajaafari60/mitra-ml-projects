# predict.py
import os
import pandas as pd
import joblib

# Path to model and data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/house_price_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "../data/Tehran-Houses-DIVAR.csv")

# Load trained model
model = joblib.load(MODEL_PATH)

# Example input for prediction
# این داده نمونه شماست؛ می‌توانید آن را تغییر دهید
example = pd.DataFrame([{
    'Area': 63,
    'Room': 1,
    'Parking': True,
    'Warehouse': True,
    'Elevator': True,
    'Address': 'Shahran',
    'Price': 1850000000,
    'Price(USD)': 61666.67
}])

# Read the full dataset for encoding reference
df = pd.read_csv(DATA_PATH, encoding='utf-8')

# Encode categorical features (Address) the same way as training
feature_names = model.feature_names_in_  # features expected by the model
sample_encoded = pd.get_dummies(example, columns=['Address', 'Parking', 'Warehouse', 'Elevator'], drop_first=False)

# Add missing columns with 0 to match training features
missing_cols = [c for c in feature_names if c not in sample_encoded.columns]
if missing_cols:
    sample_encoded = pd.concat(
        [sample_encoded, pd.DataFrame(0, index=sample_encoded.index, columns=missing_cols)],
        axis=1
    )

# Reorder columns to match training
sample_encoded = sample_encoded[feature_names]

# Make prediction
pred = model.predict(sample_encoded)

# Display result
print(f"💰 Predicted house price: {int(pred[0]):,} Rial")
