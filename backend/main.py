from fastapi import FastAPI
from routers import threats

app = FastAPI(title="PhantomShield Threat Intelligence API")

# Include API Routes
app.include_router(threats.router)

@app.get("/")
def root():
    return {"message": "PhantomShield API is running"}
