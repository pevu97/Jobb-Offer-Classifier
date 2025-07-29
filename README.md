# 👨‍💻 Job Posting Classifier API 👨‍💻

This project is a complete pipeline for classifying job offers into three experience levels: **Junior**, **Mid**, and **Senior**. It uses a Convolutional Neural Network (CNN) trained on job listings from the NoFluffJobs platform. The model is deployed via a FastAPI interface and includes elements of MLOps with MLflow.

---

## 🔧 Project Structure

```
job_classifier/
├── notebook/
  └── notebook.ipynb  # Notebook for training the model and logging with MLflow
├── app/
│   ├── main.py           # FastAPI endpoint
│   ├── model_loader.py   # Loads model and tokenizer
│   ├── predictor.py      # Prediction logic
│   └── preprocess.py     # Text preprocessing (cleaning, tokenization, padding)
│   └── requirements.txt
│   └── job_level_classifier.h5
├── README.md
```

---

## 🚀 Technologies Used

- TensorFlow / Keras (CNN model)
- FastAPI (API interface)
- MLflow (MLOps - model tracking & logging)
- BeautifulSoup, re (text cleaning)
- Tokenizer & Padding
- Anaconda environment
- Swagger UI for interaction with the API

---

## 📊 Training

The model was trained using text from real job listings, with the following architecture:

- **Embedding Layer**: output_dim=100
- **Conv1D Layer**: filters=8, kernel_size=2, ReLU
- **Global Max Pooling**
- **Dense Layer**: 16 units + L2 regularization + dropout
- **Output Layer**: 3 units (softmax)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/newplot-2.png)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/newplot-3.png)


---

## 🌐 API Endpoint

Run the API:

```
uvicorn main:app --reload
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Example request:

```json
POST /predict
{
  "text": "We are looking for a software engineer..."
}
```
![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/oferta.jpg)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/api1.jpg)

![Samples](https://kocotmeble.com/wp-content/uploads/2025/07/api2.jpg)

---

## 🧪 MLOps with MLflow

The project uses MLflow to track:

- Model architecture and parameters
- Accuracy / loss metrics
- Artifacts (e.g., trained model file)


---

## 📦 Requirements

Install all dependencies with:

```
pip install -r requirements.txt
```

---

## ✅ Project Goals

This project was created as a **portfolio piece** to showcase:
- End-to-end ML project skills
- Text classification
- FastAPI deployment
- Basic MLOps integration
