import tensorflow as tf
import pickle

def load_model_and_tokenizer():
    model = tf.keras.models.load_model("job_offer_classifier.keras")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer