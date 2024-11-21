from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load(r'c:\Users\aksha\Desktop\global earthquake\models\random_forest_model.pkl')
scaler = joblib.load(r'c:\Users\aksha\Desktop\global earthquake\models\scaler.pkl')

# Define features
features = ['latitude', 'longitude', 'depth', 'nst', 'gap', 'dmin']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        input_data = [float(request.form[feature]) for feature in features]
        
        # Scale the input and predict
        scaled_input = scaler.transform([input_data])
        prediction = model.predict(scaled_input)
        
        # Render results page
        return render_template('results.html', prediction=round(prediction[0], 2))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
