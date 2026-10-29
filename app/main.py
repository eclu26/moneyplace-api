from fastapi import FastAPI

app = FastAPI(
    title="MoneyPlace API",
    version="1.0.0"
)

@app.get("/status")
async def get_status() -> dict:
    return {"status": "operating"}