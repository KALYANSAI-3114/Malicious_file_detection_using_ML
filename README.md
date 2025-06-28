# 🛡️ Malicious File Detector Using Machine Learning

A lightweight web-based application that detects whether an uploaded file is **malicious or benign** using a trained machine learning model on byte-level signatures. Built with Flask and scikit-learn, this app provides a modern UI to test files safely and easily.

---

## 🚀 Features

- 📤 Upload `.bin`, `.exe`, or other binary files
- ⚙️ ML model trained using `RandomForestClassifier` on file byte signatures
- 💻 Clean and responsive web UI (Bootstrap-powered)
- 🧪 Safe to test — uses synthetic data only
- ✅ Instant result shown: "Malicious" or "Benign"

---

## 🧠 How It Works

1. **Data Generation**
   - `generate_dataset.py` creates:
     - Benign files: structured, repeated patterns
     - Malicious files: high-entropy random bytes

2. **Model Training**
   - `train_signature_model.py` reads the files
   - Extracts first 256 bytes per file
   - Trains a `RandomForestClassifier`
   - Saves model to `model/signature_ml_model.pkl`

3. **Prediction (Web App)**
   - Flask app (`app/main.py`) loads the model
   - User uploads a file
   - App predicts and displays the result


