from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel, ConfigDict
from services.prediction_service import predict_house_price

# Initialize the router to be registered in app.py
router = APIRouter()

# Define strictly typed validation schema for the JSON payload
class PredictionRequest(BaseModel):
    city: str
    locality_tier: str
    bhk: int
    bathrooms: int
    super_area_sqft: float
    property_age_years: float
    parking: int
    furnishing: str
    gated_society: int
    floor_no: int
    total_floors: int
    
    # Strictly forbid arbitrary fields
    model_config = ConfigDict(extra='forbid')

@router.post("/predict")
async def predict_price(request: Request, payload: PredictionRequest):
    """
    Accepts standardized house parameters and returns a log-reversed 
    monetary price prediction executed by the XGBoost engine.
    """
    try:
        # 1. Retrieve the pre-loaded model and scaler references from the app bootstrap
        model = request.app.state.model
        scaler = request.app.state.scaler
        
        # Guard clause if the backend failed to load `.pkl` artifacts on boot
        if model is None or scaler is None:
            raise RuntimeError("Machine learning artifacts are currently unavailable.")
        
        # 2. Extract validated payload to a standard python dictionary
        input_data = payload.model_dump()
        
        # 3. Delegate to orchestration service layer
        predicted_price = predict_house_price(input_data, model, scaler)
        
        # 4 & 5. Serialize prediction to required JSON envelope
        return {"predicted_price": predicted_price}
        
    except ValueError as ve:
        # Capture strictly generated downstream payload errors natively
        raise HTTPException(
            status_code=500,
            detail="The prediction engine encountered a calculation issue with the provided input."
        )
    except RuntimeError as re:
        # Capture missing model state errors
        raise HTTPException(
            status_code=503,
            detail="The prediction service is temporarily unavailable."
        )
    except Exception as e:
        # Fallback mask for unhandled backend exceptions to prevent footprint leaks
        raise HTTPException(
            status_code=500,
            detail="An internal error occurred while processing the prediction request."
        )
