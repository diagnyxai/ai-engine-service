# AI Engine Service

Centralized AI/ML service for the Diagnyx platform, providing model management, training, and inference capabilities.

## Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Database**: PostgreSQL
- **ML Libraries**: (Simplified for testing)
- **Port**: 8082 (HTTP)

## Features

- Machine learning model management
- Real-time inference API
- Model performance monitoring
- Centralized AI capabilities for other services

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/predict` | POST | Make predictions using ML models |
| `/api/v1/models` | GET | List available models |
| `/api/v1/models/{name}` | GET | Get model details |
| `/health` | GET | Service health check |
| `/metrics` | GET | Service metrics |

## Running Locally

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the service
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8082
```

## Database Configuration

The service is configured to use PostgreSQL:

```python
# Database connection (to be implemented)
DATABASE_URL = "postgresql://dev:dev@localhost:5432/dgx-dev"
```

## API Documentation

When running, API documentation is available at:
- Swagger UI: http://localhost:8082/docs
- ReDoc: http://localhost:8082/redoc

## Health Check

```
http://localhost:8082/health
``` 