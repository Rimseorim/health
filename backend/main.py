from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, records

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CrossFit Rehab API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(records.router)

@app.get("/")
def root():
    return {"status": "ok"}
