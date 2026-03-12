# 🧠 House Price Prediction Model

This repository contains the **machine learning model training pipeline** used for predicting house prices.  
The model was trained using real estate datasets and focuses on learning relationships between property features and market price.

The goal of this project is to build a **robust regression model** capable of estimating property prices based on location, amenities, and structural features.

---

# 📊 Dataset

Two datasets were used during the development of this model.

## 1️⃣ Cost Estimation Dataset

Used initially to understand construction cost patterns.

Features included:

- Material_Cost  
- Labor_Cost  
- Profit_Rate  
- Discount_or_Markup  
- Policy_Reason  
- Total_Estimate  

Purpose of this dataset:

- Understand pricing patterns
- Practice preprocessing and model evaluation
- Build the initial regression pipeline

---

## 2️⃣ Housing Market Dataset (Primary Dataset)

This dataset contains **12,000 property records** with multiple features describing house characteristics.

Main features include:

| Feature | Description |
|------|------|
| City | City where property is located |
| Locality_Tier | Area category (Basic / Mid / Premium) |
| BHK | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Super_Area_sqft | Total area of property |
| Carpet_Area_sqft | Usable living area |
| Floor_No | Floor number |
| Total_Floors | Total floors in building |
| Property_Age_years | Age of the property |
| Parking | Parking availability |
| Furnishing | Furnishing level |
| Lift | Lift availability |
| Gated_Society | Whether property is in gated community |
| Distance_to_Metro_km | Distance to nearest metro |
| Distance_to_CityCenter_km | Distance to city center |
| Nearby_School_km | Distance to nearest school |
| Nearby_Hospital_km | Distance to nearest hospital |
| Crime_Rate_Index | Local crime index |
| Market_Price_INR | Market price of property |
| Price_per_sqft_INR | Price per square foot |

Target Variable:

Market_Price_INR

---

# ⚙️ Data Preprocessing

Before training the model, several preprocessing steps were performed.

## 1️⃣ Data Cleaning

- Checked dataset structure using `df.info()` and `df.shape()`
- Verified data types
- Checked missing values
- Removed unnecessary columns such as `House_ID`

---

## 2️⃣ Encoding Categorical Variables

Categorical columns were converted into numerical features using **One-Hot Encoding**.

Columns encoded:

- City
- Locality_Tier
- Furnishing

Example encoded features:

City_Pune  
City_Mumbai  
City_Nagpur  
City_Hyderabad  

---

## 3️⃣ Feature Engineering

Additional transformations were applied:

- Removed `Price_per_sqft_INR` to avoid **data leakage**
- Applied **log transformation** to the target variable to stabilize variance

Target transformation:

y = log(Market_Price_INR)

This helps regression models perform better on skewed price distributions.

---

## 4️⃣ Feature Scaling

Features were standardized using **StandardScaler**.

This ensures that all numerical features have similar distributions and improves model performance for algorithms sensitive to feature scale.

---

## 5️⃣ Train-Test Split

The dataset was divided into training and testing sets.

Training Data: 80%  
Testing Data: 20%

This allows proper evaluation of model performance on unseen data.

---

# 🤖 Models Trained

Multiple regression algorithms were trained and compared.

Models used:

1. Linear Regression  
2. Random Forest Regressor  
3. Gradient Boosting Regressor  
4. XGBoost Regressor  

Training multiple models helped identify which algorithm performs best for this dataset.

---

# 📈 Model Evaluation

The following metrics were used to evaluate model performance.

| Metric | Description |
|------|------|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| R² Score | Measures how well the model explains variance |

These metrics help measure prediction accuracy and model reliability.

---

# 🏆 Best Performing Model

After evaluating all models, **XGBoost Regressor** produced the best performance.

Example performance comparison:

| Model | R² Score |
|------|------|
| Linear Regression | ~0.95 |
| Random Forest | ~0.98 |
| Gradient Boosting | ~0.98 |
| **XGBoost** | **~0.986** |

XGBoost provided the best balance between accuracy and generalization.

---

# 💾 Model Saving

The trained model and preprocessing scaler were saved using **Joblib**.

Saved artifacts:

house_price_model.pkl  
scaler.pkl  

These files are later used for prediction during application runtime.

---

# 🔄 Model Training Workflow

Dataset Collection  
↓  
Data Cleaning  
↓  
Exploratory Data Analysis (EDA)  
↓  
Feature Engineering  
↓  
Categorical Encoding  
↓  
Feature Scaling  
↓  
Train-Test Split  
↓  
Model Training  
↓  
Model Evaluation  
↓  
Best Model Selection  
↓  
Model Export (.pkl)

---

# 📓 Training Notebook

The full training process is documented in the Jupyter notebook:

house_price_model_training.ipynb

The notebook includes:

- Data exploration
- Feature analysis
- Model training
- Model comparison
- Model export

---

# 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- XGBoost  
- Matplotlib  
- Jupyter Notebook  

---

# 📌 Conclusion

This project demonstrates the complete workflow of building a **machine learning regression model for house price prediction**.

The pipeline includes:

- Data preprocessing
- Feature engineering
- Multiple model training
- Performance evaluation
- Exporting the best model

The trained model can estimate property prices using structural and location-based features, making it useful for real estate analytics and decision support systems.
