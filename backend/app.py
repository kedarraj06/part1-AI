import os
import joblib
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

PORT = os.getenv("PORT", "8000")
MODEL_PATH = os.getenv("MODEL_PATH", "model/house_price_model.pkl")
SCALER_PATH = os.getenv("SCALER_PATH", "model/scaler.pkl")
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN", "*")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load ML model and scaler once at startup
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Resolve paths (handling if they are relative from the backend directory)
    absolute_model_path = os.path.join(base_dir, MODEL_PATH) if not os.path.isabs(MODEL_PATH) else MODEL_PATH
    absolute_scaler_path = os.path.join(base_dir, SCALER_PATH) if not os.path.isabs(SCALER_PATH) else SCALER_PATH

    try:
        app.state.model = joblib.load(absolute_model_path)
        app.state.scaler = joblib.load(absolute_scaler_path)
        print("Model and scaler loaded successfully.")
    except Exception as e:
        print(f"Error loading model or scaler during startup: {e}")
        app.state.model = None
        app.state.scaler = None

    yield
    
    # Clear memory structures gracefully on shutdown
    app.state.model = None
    app.state.scaler = None

# Initialize FastAPI application
app = FastAPI(title="AI House Price Prediction API", lifespan=lifespan)

# Enable CORS using ALLOWED_ORIGIN from the .env file
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN] if ALLOWED_ORIGIN != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and register router
try:
    from routes.predict import router as predict_router
    app.include_router(predict_router)
except ImportError:
    print("Warning: routes.predict router not found or not implemented yet. Skipping router registration.")

# Basic global error handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred processing the request.",
            "details": str(exc)
        }
    )

# Root health check endpoint
@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": "house-price-api"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(PORT), reload=True)
