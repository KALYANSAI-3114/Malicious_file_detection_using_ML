import os
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from utils.signature_utils import extract_signature_bytes

mal_dir = "data/malicious_samples"
ben_dir = "data/benign_samples"
X, y = [], []

# Load malicious samples
for file in os.listdir(mal_dir):
    path = os.path.join(mal_dir, file)
    X.append(extract_signature_bytes(path))
    y.append(1)

# Load benign samples
for file in os.listdir(ben_dir):
    path = os.path.join(ben_dir, file)
    X.append(extract_signature_bytes(path))
    y.append(0)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/signature_ml_model.pkl")
print("✅ Model trained and saved to model/signature_ml_model.pkl")
