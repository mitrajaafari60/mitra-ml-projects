# evaluate_model.py
import joblib
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

def evaluate_model(X_valid, y_valid):
    model = joblib.load("../models/house_price_model.pkl")
    preds = model.predict(X_valid)
    
    print("📊 Model evaluation results:")
    print(f"R² Score: {r2_score(y_valid, preds):.3f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_valid, preds)):.2f}")

if __name__ == "__main__":
    from preprocess import preprocess_data
    from data_analysis import explore_data
    df = explore_data()
    X_train, X_valid, y_train, y_valid = preprocess_data(df)
    evaluate_model(X_valid, y_valid)
