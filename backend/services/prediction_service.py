import numpy as np
import pandas as pd
from utils.feature_engineering import prepare_features

def predict_house_price(input_data: dict, model, scaler) -> float:
    """
    Orchestrates the full ML prediction pipeline for house prices.
    Generates features, scales them, runs inference, and reverses the log transform.
    """
    try:
        # Step 1: Feature Engineering
        # Transforms the raw dictionary into a perfectly ordered 23-column DataFrame
        features_df = prepare_features(input_data)
        
        # Step 2: Scale Features
        # Transform using the pre-fitted StandardScaler loaded in memory
        scaled_features = scaler.transform(features_df)
        
        # Step 3: Run Model Prediction
        # The XGBoost model predicts the logarithmic value of the house price
        log_predicted_price = model.predict(scaled_features)
        
        # Step 4: Reverse Log Transformation
        # Apply exponential function to convert the log price back to a real currency value
        real_price = np.exp(log_predicted_price[0])
        
        # Step 5: Return Final Price
        return float(real_price)
        
    except Exception as e:
        # Catch any pipeline failures gracefully and raise a clean sanitized error message
        raise ValueError(f"Prediction pipeline failed during execution: {str(e)}")
