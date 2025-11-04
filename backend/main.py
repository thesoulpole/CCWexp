from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Hello API", description="A simple FastAPI application")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HelloResponse(BaseModel):
    message: str
    status: str
    name: Optional[str] = None

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Hello API!", "status": "online"}

@app.get("/api/hello", response_model=HelloResponse)
async def hello(name: Optional[str] = None):
    """
    Say hello!

    - **name**: Optional name to personalize the greeting
    """
    if name:
        message = f"Hello, {name}! Welcome to our FastAPI application!"
    else:
        message = "Hello, World! Welcome to our FastAPI application!"

    return {
        "message": message,
        "status": "success",
        "name": name
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "hello-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
