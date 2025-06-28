import sys
import os
from flask import Flask, render_template, request
import joblib

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import signature_utils relative to the project root
# Assuming 'utils' is a directory at the project root
try:
    from utils.signature_utils import extract_signature_bytes
except ImportError:
    # Fallback for local testing if path issues persist
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
    from signature_utils import extract_signature_bytes


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'uploads'))
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model using full path
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model', 'signature_ml_model.pkl'))
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model file not found at: {model_path}\n➡️ Please run train_signature_model.py first.")
model = joblib.load(model_path)

@app.route('/')
def home():
    # On initial GET request, we ensure 'result' is None and 'scan_performed' is False.
    # This prevents the result div from showing.
    return render_template('index.html', result=None, scan_performed=False)

@app.route('/predict', methods=['POST'])
def predict():
    label = None # Initialize label to None
    scan_performed_flag = True # Set flag to True when predict route is hit

    if 'file' not in request.files:
        label = "No file part in request."
    else:
        file = request.files['file']
        if file.filename == '':
            label = "No selected file."
        else:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                # Save the file. Ensure the 'uploads' directory exists.
                file.save(file_path)
                # Extract features using the utility function
                features = extract_signature_bytes(file_path)
                # Make prediction using the loaded model
                prediction = model.predict([features])[0]
                # Determine the label based on prediction
                label = "Malicious" if prediction == 1 else "Benign"
            except Exception as e:
                # Catch any errors during file processing or prediction
                label = f"Error during scan: {str(e)}"
            finally:
                # Clean up: remove the uploaded file after processing
                if os.path.exists(file_path):
                    os.remove(file_path)

    # Always render the template with the result and the scan_performed flag
    return render_template('index.html', result=label, scan_performed=scan_performed_flag)

if __name__ == '__main__':
    # It's good practice to run in debug mode only during development
    # For production, set debug=False and use a production-ready WSGI server
    app.run(debug=True)
