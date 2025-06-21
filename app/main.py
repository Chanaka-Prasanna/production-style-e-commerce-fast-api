from fastapi import FastAPI

app = FastAPI(title="E commerce  Backend")

@app.get('/')
async def read_root():
    return {"message":"Hello, World from E commerce - Backend"}