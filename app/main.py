from fastapi import FastAPI
from app.api.v1 import products, users

app = FastAPI(title="E commerce  Backend")
app.include_router(products.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get('/')
async def read_root():
    return {"message":"Hello, World from E commerce - Backend"}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}