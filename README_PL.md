# 👨‍💻 Job Posting Classifier API 👨‍💻

Projekt służy do klasyfikacji poziomu doświadczenia wymaganego w ogłoszeniu o pracę – `junior`, `mid` lub `senior`.

---

## 🔧 Struktura projektu

```
job_classifier/
├── notebook/
  └── notebook.ipynb  # Notebook do treningu modelu
├── app/
│   ├── main.py           # FastAPI – punkt wejścia do API
│   ├── model_loader.py   # Ładowanie modelu i tokenizer'a
│   ├── predictor.py      # Funkcja predykcji
│   └── preprocess.py     # Czyszczenie i tokenizacja tekstu
│   └── requirements.txt
│   └── job_level_classifier.h5
├── README.md
```

---

## 🚀 Technologies Used

- Warstwa `Embedding`
- Warstwa `Conv1D` z `filters=8`, `kernel_size=2`
- `Dropout`
- `GlobalMaxPooling1D`
- `Dense + ReLU + Dropout`
- `Dense + Softmax`

Wytrenowany na ofertach pracy pobranych z portalu NoFluffJobs API (ok. 2000 ofert)
---

## 📊 Training

W notebooku `training_notebook.ipynb`:

- Tokenizacja
- Padding
- Podział na dane treningowe i testowe
- Trening CNN
- Zapisywanie modelu `.h5` oraz tokenizer `.pkl`
- Logowanie parametrów za pomocą MLflow

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/newplot-2.png)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/newplot-3.png)


---

## 🌐 API Endpoint

Aby uruchomić serwer lokalnie:

```bash
uvicorn main:app --reload
```

Następnie przejdź do dokumentacji API:

👉 http://127.0.0.1:8000/docs

Endpoint `/predict` przyjmuje JSON:

```json
{
  "text": "Treść oferty pracy do klasyfikacji..."
}
```

Zwraca:

```json
{
  "predicted_label": "mid"
}
```
![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/oferta.jpg)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/api1.jpg)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/api2.jpg)

---

## 🧪 MLOps

Projekt wspiera:

- MLflow – do logowania eksperymentów (parametry, metryki, artefakty)
- Możliwość dalszej integracji z Dockerem i CI/CD


---

## 📦 Requirements

Zainstaluj wszystkie biblioteki:

```
pip install -r requirements.txt
```

---

## ✅ Cel projektu

- dodanie testów jednostkowych
- możliwość trenowania nowego modelu z poziomu API
- logowanie predykcji
