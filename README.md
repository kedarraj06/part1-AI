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
