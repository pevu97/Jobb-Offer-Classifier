from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model_and_tokenizer
from predictor import predict_label

app = FastAPI()

class InputData(BaseModel):
    text: str
    
model, tokenizer = load_model_and_tokenizer()

@app.post("/predict")
def predict(input_data: InputData):
    label = predict_label(input_data.text, model, tokenizer)
    return {"predicted_label": label}