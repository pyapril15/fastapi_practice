# Import required modules
from fastapi import FastAPI         # FastAPI web framework
import uvicorn                      # ASGI server to run FastAPI apps
import os                           # For accessing environment variables
from dotenv import load_dotenv      # To load .env file variables into environment

# Load environment variables from the .env file
load_dotenv()

# Create an instance of the FastAPI app
app = FastAPI(
    title="FastAPI Practice API",    # Title shown in Swagger docs
    version="1.0.0",                 # Version number of your API
    description="A simple practice FastAPI app"  # Optional description
)

# Root route - returns a welcome message
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to confirm that the API is running.
    """
    return {"message": "Hello from FastAPI!"}

# Health check route - used for monitoring or Render health checks
@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint for uptime monitoring or platform health checks.
    """
    return {"status": "ok"}

# Run the app only if the script is executed directly (not imported)
if __name__ == "__main__":
    # Get the HOST and PORT from environment variables
    # If not found, use the default values: "127.0.0.1" and 8000
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))

    # Run the FastAPI app with uvicorn
    uvicorn.run(
        "main:app",              # 'main' is the filename, 'app' is the FastAPI instance
        host=host,               # Host address (from .env or default)
        port=port,               # Port number (from .env or default)
        reload=True if host == "127.0.0.1" else False  # Reload enabled only for local dev
    )
