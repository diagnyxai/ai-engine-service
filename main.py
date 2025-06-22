"""
Simplified AI Engine Service for Testing
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List
import time
import random
import psycopg2

# Simple models
class InferenceRequest(BaseModel):
    model_name: str
    features: Dict[str, Any]

class InferenceResponse(BaseModel):
    model_name: str
    prediction: Any
    confidence: float
    timestamp: int
    processing_time_ms: float

class HealthResponse(BaseModel):
    status: str
    version: str
    uptime: float
    service: str
    database: str

class ServiceStatusResponse(BaseModel):
    service: str
    timestamp: str
    database: str
    status: str
    message: str

# Database configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "ai-engine-db"
DB_USER = "dev"
DB_PASSWORD = "dev"

# Create FastAPI app
app = FastAPI(
    title="Diagnyx AI Engine Service",
    description="Simplified AI engine service for testing",
    version="1.0.0"
)

# Store start time for uptime calculation
start_time = time.time()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "AI Engine Service",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    # Simple database connection check
    db_status = "UP"
    try:
        # For simplicity, we're not actually connecting to the database
        # In a real service, you would check the connection here
        pass
    except Exception:
        db_status = "DOWN"
        
    return HealthResponse(
        status="UP",
        version="1.0.0", 
        uptime=time.time() - start_time,
        service="ai-engine-service",
        database=db_status
    )

@app.get("/service-status", response_model=ServiceStatusResponse)
async def service_status():
    """Service status endpoint for database connectivity check"""
    db_status = "UP"
    status = "SUCCESS"
    message = "AI Engine Service is operational with database connectivity"
    
    try:
        # Attempt to connect to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
    except Exception as e:
        db_status = "DOWN"
        status = "FAILURE"
        message = f"AI Engine Service is degraded - database connectivity issue: {str(e)}"
    
    return ServiceStatusResponse(
        service="ai-engine-service",
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        database=db_status,
        status=status,
        message=message
    )

@app.post("/api/v1/predict", response_model=InferenceResponse)
async def predict(request: InferenceRequest):
    """Inference endpoint"""
    # Simulate AI prediction
    start_process = time.time()
    
    # Generate a random prediction based on the model name
    if "anomaly" in request.model_name:
        prediction = random.choice(["normal", "anomaly"])
        confidence = random.uniform(0.7, 0.99)
    elif "forecast" in request.model_name:
        prediction = {
            "next_hour": random.uniform(80, 120),
            "next_day": random.uniform(70, 130),
            "next_week": random.uniform(60, 140)
        }
        confidence = random.uniform(0.6, 0.95)
    else:
        prediction = random.uniform(0, 100)
        confidence = random.uniform(0.5, 0.99)
    
    processing_time = (time.time() - start_process) * 1000
    
    return InferenceResponse(
        model_name=request.model_name,
        prediction=prediction,
        confidence=confidence,
        timestamp=int(time.time()),
        processing_time_ms=processing_time
    )

@app.get("/metrics")
async def metrics():
    """Metrics endpoint"""
    return {
        "inference_requests": 42,
        "active_models": 3,
        "average_inference_time": 25.5
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8082) 