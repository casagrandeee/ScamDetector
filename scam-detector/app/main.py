from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Scam Ad Detector API is running"}

@app.post("/verify")
def verify_ad(payload: dict):
    text = payload.get("text", "")
    return {"result": "received", "text":text}