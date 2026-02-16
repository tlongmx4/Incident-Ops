from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.routes import users, incidents


app = FastAPI(title="Incident Ops API", version="1.0")

@app.on_event("startup")
def startup_event():
    # Initialize database connection or other startup tasks here
    pass

@app.get("/")
def read_root():
    return {"message": "Welcome to the Incident Ops API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(incidents.router)
app.include_router(users.router)