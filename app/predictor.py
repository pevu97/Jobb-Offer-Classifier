import numpy as np
from preprocess import preprocess_input

label_map = {0: "junior", 1: "mid", 2: "senior"}

def predict_label(text, model, tokenizer):
    processed = preprocess_input(text, tokenizer)
    prediction = model.predict(processed)
    label_index = np.argmax(prediction, axis=1)[0]
    return label_map[label_index]
