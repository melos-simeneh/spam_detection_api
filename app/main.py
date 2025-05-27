from fastapi import FastAPI
from app.model import load_model, predict_message
from app.schemas import Message

app = FastAPI(title="Spam Detection API")

model = load_model()

@app.get("/")
def read_root():
    return {"message": "Spam Detection API is running!"}

@app.post("/predict")
def predict_spam(data: Message):
    result = predict_message(model, data.text)
    return {"prediction": result}
