<<<<<<< HEAD
# AI House Price Prediction System

## Overview

This project is an **AI-powered house price prediction system** that estimates the **market value of residential properties** based on various property features.
It uses **machine learning (XGBoost)** trained on housing datasets and provides predictions through a **web interface**.

Users enter property details such as location, area, number of rooms, and amenities, and the system predicts the **estimated market price of the house**.

---

## Project Goal

The goal of this project is to build an **end-to-end AI application** that integrates:

* Machine Learning model training
* Backend API for predictions
* Frontend dashboard for user interaction

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost

### Backend

* Python (FastAPI / Flask)
* Joblib
* REST API

### Frontend

* React

---

## Machine Learning Pipeline

The model was trained using the following pipeline:

1. Import required libraries
2. Data preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature selection
5. Feature scaling
6. Train-test split
7. Model training
8. Model evaluation
9. Model selection
10. Model saving

Multiple models were tested:

* Linear Regression
* Random Forest
* Gradient Boosting
* XGBoost

The **XGBoost model performed the best** and was selected as the final model.

---

## Model Inputs

The prediction model uses the following features:

* City
* Locality Tier
* BHK
* Bathrooms
* Super Area (sqft)
* Carpet Area (sqft)
* Floor Number
* Total Floors
* Property Age
* Parking
* Lift
* Gated Society
* Distance to Metro
* Distance to City Center
* Distance to School
* Distance to Hospital
* Crime Rate Index
* Furnishing Type

---

## Model Output

The model predicts:

**Estimated Market Price of the House (INR)**

---

## Project Workflow

User → Frontend Form → Backend API → Machine Learning Model → Prediction

1. User enters property details on the dashboard
2. Frontend sends data to backend API
3. Backend prepares the feature vector
4. Model predicts price
5. Prediction is returned to the frontend
6. User sees the estimated house price

---

## Project Structure

```
project/
│
├── backend
│   ├── model
│   │   ├── house_price_model.pkl
│   │   └── scaler.pkl
│   │
│   ├── routes
│   ├── services
│   ├── utils
│   │
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── .env.example
│
├── Frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── services
│   │
│   ├── package.json
│   ├── .env
│   └── .env.example
│
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```
git clone <repository-url>
cd project
```

---

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
python app.py
```
*(The backend runs on `http://localhost:5000` by default)*

---

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd Frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```
*(The frontend runs on `http://localhost:5173` or `http://localhost:5174` depending on availability)*

---

## API Endpoint

### Predict House Price

```
POST /predict
```

Example request:

```
{
  "city": "Pune",
  "bhk": 3,
  "bathrooms": 2,
  "super_area_sqft": 1200,
  "property_age": 5
}
```

Response:

```
{
  "predicted_price": 7800000
}
```

---

## Future Improvements

* Add user authentication
* Add property comparison
* Add price trend analysis
* Integrate real estate datasets
* Deploy the model on cloud

---

## Author

Project developed as an **AI + Full Stack Machine Learning project**.

---
=======
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
>>>>>>> 9705ed22df9cd618e8d1823d8eeb5cd66505c524
