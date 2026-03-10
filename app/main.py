from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.modules import products

app = FastAPI(
    title="Butterfly API",
    description="Local API for serving product data and 3D model metadata",
    version="1.0.0"
)

# Mount static files
app.mount("/public", StaticFiles(directory="app/public"), name="public")

# Include product routes
app.include_router(products.router)


@app.get("/")
def root():
    return {
        "service": "Butterfly API",
        "status": "running"
    }
