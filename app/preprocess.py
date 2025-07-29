import re
from bs4 import BeautifulSoup
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LEN = 200  # taka jak przy trenowaniu

def clean_text(text: str) -> str:
    # Zamień znaki kontrolne (enter, tabulacje, itp.) na spacje
    text = re.sub(r'[\r\n\t\x0b\x0c]', ' ', text)

  # Zamień wszystkie znaki nie-alfanumeryczne na spację
    text = re.sub(r'\W+', ' ', text)
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'\W+', ' ', text)
    return text.lower().strip()

def preprocess_input(text: str, tokenizer) -> list:
    cleaned = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)
    return padded
