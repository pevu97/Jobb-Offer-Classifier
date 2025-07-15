# 🧥 Vinted Gender Classifier

Klasyfikator płci ogłoszenia z platformy Vinted na podstawie tytułu, opisu i tagów. Projekt typu end-to-end — zawiera cały cykl tworzenia rozwiązania ML na poziomie produkcyjnym, łącznie z wdrożeniem modelu jako REST API.

---

## 📌 Cel projektu

Stworzenie systemu ML, który automatycznie klasyfikuje ogłoszenia jako przeznaczone dla kobiet lub mężczyzn. Projekt może służyć jako baza do:

- filtrowania ogłoszeń,
- segmentacji użytkowników,
- analizy trendów modowych.

---

## 🛠️ Stack technologiczny

| Komponent           | Technologia                                |
|---------------------|---------------------------------------------|
| Scraping danych     | `requests`, `BeautifulSoup`, `Selenium`     |
| Preprocessing       | `pandas`, `scikit-learn`, `nltk`            |
| Modelowanie         | `scikit-learn` (LogisticRegression, etc.)   |
| Eksperymenty        | `MLflow`                                    |
| Serializacja modeli | `joblib`                                    |
| API predykcyjne     | `FastAPI`                                   |

---

## 🗂️ Struktura projektu

vinted-gender-classifier/
├── data/                   # Surowe lub przetworzone dane
├── notebooks/              # EDA, prototypy, eksperymenty
├── src/                    # Logika aplikacji ML
│   ├── scraper.py
│   ├── preprocess.py
│   ├── train.py
│   ├── model_utils.py
├── api/                    # REST API oparte na FastAPI
│   └── main.py
├── mlruns/                 # Folder wygenerowany przez MLflow
├── requirements.txt
├── README.md
└── .gitignore

---

## ▶️ Jak uruchomić projekt lokalnie

### 1. Klonuj repozytorium
git clone https://github.com/twoj-login/vinted-gender-classifier.git
cd vinted-gender-classifier

### 2. Zainstaluj zależności
pip install -r requirements.txt

### 3. Scraping danych (opcjonalnie)
python src/scraper.py

### 4. Trening modelu z MLflow
python src/train.py
mlflow ui

Interfejs MLflow będzie dostępny pod adresem: http://localhost:5000

### 5. Uruchomienie REST API
uvicorn api.main:app --reload

API będzie dostępne pod adresem: http://localhost:8000

---

## 📦 Przykładowe użycie API

### POST `/predict`
{
  "title": "Granatowa koszula męska slim fit",
  "description": "Elegancka, idealna na spotkania biznesowe"
}

### Response:
{
  "prediction": "Męskie",
  "confidence": 0.87
}

---

## 📊 Przykład wyników MLflow

- Model: LogisticRegression
- Accuracy: 87.4%
- TF-IDF + tokenizacja
- Dane: 2500 ogłoszeń z Vinted (równomiernie podzielone)

---

## 🔬 Możliwe rozszerzenia

- Klasyfikacja na więcej klas (np. dziecięce, unisex)
- Wykorzystanie obrazów z ogłoszeń
- Dodanie retrainingu z nowych danych
- Hosting modelu online (Render, Hugging Face Spaces)
- Docker + CI/CD

---

## 📄 Licencja

Projekt powstał wyłącznie w celach edukacyjno-portfolio. Nie jest powiązany z platformą Vinted.
