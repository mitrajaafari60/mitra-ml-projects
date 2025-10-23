# preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import os
import joblib

def preprocess_data(df):
    df = df.dropna(subset=['Price'])  # remove rows with missing target
    X = df.drop(['Price'], axis=1)
    y = df['Price']

    # One-hot encode categorical columns
    X = pd.get_dummies(X)

    # Split into train/validation
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=42)
    
    print("✅ Data preprocessing done!")
    print("Training shape:", X_train.shape)
    print("Validation shape:", X_valid.shape)
    joblib.dump(X_train.columns.tolist(), "../models/features_list.pkl")
    print("💾 Saved feature list for prediction step.")
    return X_train, X_valid, y_train, y_valid

if __name__ == "__main__":
    from data_analysis import explore_data
    df = explore_data()
    if df is not None:
        preprocess_data(df)
        