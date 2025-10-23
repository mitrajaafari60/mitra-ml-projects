# train_model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(X_train, y_train, X_valid, y_valid):
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    mae = mean_absolute_error(y_valid, preds)
    
    print(f"✅ Model trained successfully! MAE = {mae:.2f}")
    
    # Save model
    joblib.dump(model, "../models/house_price_model.pkl")
    print("💾 Model saved to models/house_price_model.pkl")

if __name__ == "__main__":
    from preprocess import preprocess_data
    from data_analysis import explore_data
    df = explore_data()
    X_train, X_valid, y_train, y_valid = preprocess_data(df)
    train_model(X_train, y_train, X_valid, y_valid)
