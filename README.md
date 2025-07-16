# 🧥 Vinted Gender Classifier

A machine learning project that classifies Vinted listings as either "male" or "female"-oriented based on their title, description, and tags. This is a full end-to-end ML pipeline designed to demonstrate commercial-level engineering skills — from data collection and training to deployment via REST API.

---

## 📌 Project Objective

Build an ML system that automatically determines whether a listing on Vinted is targeted at women or men. Potential use cases include:

- Automated content tagging,
- User segmentation,
- Fashion trend analysis.

---

## 🛠️ Tech Stack

| Component              | Technology                                  |
|------------------------|----------------------------------------------|
| Data Scraping          | `requests`, `BeautifulSoup`, `Selenium`      |
| Preprocessing          | `pandas`, `scikit-learn`, `nltk`             |
| Modeling               | `scikit-learn` (LogisticRegression, etc.)    |
| Experiment Tracking    | `MLflow`                                     |
| Model Serialization    | `joblib`                                     |
| API Deployment         | `FastAPI`                                    |

---

## 🗂️ Project Structure

vinted-gender-classifier/
├── data/                   # Raw or preprocessed data  
├── notebooks/              # EDA, experiments  
├── src/                    # Core ML logic  
│   ├── scraper.py  
│   ├── preprocess.py  
│   ├── train.py  
│   ├── model_utils.py  
├── api/                    # FastAPI prediction endpoint  
│   └── main.py  
├── mlruns/                 # MLflow logging directory  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/pevu97/Vinted-Gender-Classifier.git
cd Vinted-Gender-Classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Scrape data
```bash
python src/scraper.py
```

### 4. Train model with MLflow
```bash
python src/train.py
mlflow ui
```

MLflow dashboard will be available at: http://localhost:5000

### 5. Start prediction API
```bash
uvicorn api.main:app --reload
```

API will be accessible at: http://localhost:8000

---

## 📦 Example API Usage

### POST `/predict`
```json
{
  "title": "Navy slim-fit men's shirt",
  "description": "Elegant, perfect for business meetings"
}
```

### Response:
```json
{
  "prediction": "Male",
  "confidence": 0.87
}
```

---

## 📊 Example MLflow Results

- Model: LogisticRegression  
- Accuracy: 87.4%  
- Features: TF-IDF + tokenization  
- Dataset: 2500 listings (balanced male/female)  

---

## 🔬 Possible Extensions

- Multi-class classification (e.g. kids, unisex)
- Add image-based model
- Automated retraining on new listings
- Online deployment (Render, Hugging Face Spaces)
- Docker + CI/CD integration

---

## 📄 License

This project is for educational and portfolio purposes only. It is not affiliated with or endorsed by Vinted.
