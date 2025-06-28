import sys
import joblib
from utils.signature_utils import extract_signature_bytes

# Ensure a file path is passed
if len(sys.argv) != 2:
    print("Usage: python predict_signature.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

# Load the trained model
model = joblib.load("model/signature_ml_model.pkl")

# Extract features and predict
features = extract_signature_bytes(file_path)
prediction = model.predict([features])[0]

print(f"Prediction: {'Malicious' if prediction == 1 else 'Benign'}")
