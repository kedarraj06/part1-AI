import pandas as pd
import numpy as np

def prepare_features(input_data: dict) -> pd.DataFrame:
    """
    Transforms raw API input data into the exact feature vector required by the
    trained XGBoost machine learning model.
    """
    
    # 1. Base input extraction
    bhk = input_data.get('bhk', 0)
    bathrooms = input_data.get('bathrooms', 0)
    super_area_sqft = input_data.get('super_area_sqft', 0)
    floor_no = input_data.get('floor_no', 0)
    total_floors = input_data.get('total_floors', 0)
    property_age_years = input_data.get('property_age_years', 0)
    parking = input_data.get('parking', 0)
    gated_society = input_data.get('gated_society', 0)
    
    # 2. Feature Engineering Rules
    carpet_area_sqft = 0.82 * super_area_sqft
    lift = 1 if total_floors > 3 else 0
    
    # 3. Default Values for Missing Features
    distance_to_metro_km = input_data.get('distance_to_metro_km', 3.0)
    distance_to_citycenter_km = input_data.get('distance_to_citycenter_km', 7.0)
    nearby_school_km = input_data.get('nearby_school_km', 1.5)
    nearby_hospital_km = input_data.get('nearby_hospital_km', 2.0)
    crime_rate_index = input_data.get('crime_rate_index', 50.0)
    
    # 4. Categorical Encoding (One-Hot)
    city = input_data.get('city', '')
    city_hyderabad = 1 if city == 'Hyderabad' else 0
    city_mumbai = 1 if city == 'Mumbai' else 0
    city_nagpur = 1 if city == 'Nagpur' else 0
    city_pune = 1 if city == 'Pune' else 0
    
    locality_tier = input_data.get('locality_tier', '')
    locality_tier_mid = 1 if locality_tier == 'Mid' else 0
    locality_tier_premium = 1 if locality_tier == 'Premium' else 0
    
    furnishing = input_data.get('furnishing', '')
    furnishing_semi_furnished = 1 if furnishing == 'Semi-Furnished' else 0
    furnishing_unfurnished = 1 if furnishing == 'Unfurnished' else 0
    
    # 5. Final Model Input Features Assembly
    # The dictionary keys must perfectly match the required columns
    feature_dict = {
        'BHK': bhk,
        'Bathrooms': bathrooms,
        'Super_Area_sqft': super_area_sqft,
        'Carpet_Area_sqft': carpet_area_sqft,
        'Floor_No': floor_no,
        'Total_Floors': total_floors,
        'Property_Age_years': property_age_years,
        'Parking': parking,
        'Lift': lift,
        'Gated_Society': gated_society,
        'Distance_to_Metro_km': distance_to_metro_km,
        'Distance_to_CityCenter_km': distance_to_citycenter_km,
        'Nearby_School_km': nearby_school_km,
        'Nearby_Hospital_km': nearby_hospital_km,
        'Crime_Rate_Index': crime_rate_index,
        'City_Hyderabad': city_hyderabad,
        'City_Mumbai': city_mumbai,
        'City_Nagpur': city_nagpur,
        'City_Pune': city_pune,
        'Locality_Tier_Mid': locality_tier_mid,
        'Locality_Tier_Premium': locality_tier_premium,
        'Furnishing_Semi-Furnished': furnishing_semi_furnished,
        'Furnishing_Unfurnished': furnishing_unfurnished
    }
    
    # 6. Return Dataframe (exactly 1 row)
    return pd.DataFrame([feature_dict])
