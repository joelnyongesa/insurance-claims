from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Loading the pretrained model
model_path = 'models/insurance_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Creating the routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Debug: Print form data to see what's being received
        print("Form data received:", request.form)
        
        # Getting the form data - using lowercase field names to match HTML form
        data = {
            'Age': float(request.form.get('age', 0)),
            'Gender': request.form.get('gender', ''),
            'Income': float(request.form.get('income', 0)),
            'Marital_Status': request.form.get('marital_status', ''),
            'Education': request.form.get('education', ''),
            'Occupation': request.form.get('occupation', ''),
        }

        # Debug: Print processed data
        print("Processed data:", data)

        # Creating the dataframe
        input_df = pd.DataFrame([data])

        # Making the prediction
        log_prediction = model.predict(input_df)
        prediction = np.expm1(log_prediction)[0]

        # Calculating the risk score.
        min_claim = 114  # From our analysis
        max_claim = 99841  # From our analysis
        risk_score = (prediction - min_claim) / (max_claim - min_claim)

        # Calculating the premium
        base_premium = 1000
        premium = base_premium * (1 + risk_score) * 1.2  # For including the profit margin

        return render_template('result.html',
                               prediction=round(prediction, 2),
                               risk_score=round(risk_score, 4),
                               premium=round(premium, 2))

    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('error.html', error=str(e))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        print("API data received:", data)
        
        # Create DataFrame with correct column names
        input_df = pd.DataFrame([{
            'Age': float(data.get('Age', data.get('age', 0))),
            'Gender': data.get('Gender', data.get('gender', '')),
            'Income': float(data.get('Income', data.get('income', 0))),
            'Marital_Status': data.get('Marital_Status', data.get('marital_status', '')),
            'Education': data.get('Education', data.get('education', '')),
            'Occupation': data.get('Occupation', data.get('occupation', ''))
        }])
        
        log_prediction = model.predict(input_df)
        prediction = np.expm1(log_prediction)[0]

        min_claim = 114  # From our analysis
        max_claim = 99841  # From our analysis
        risk_score = (prediction - min_claim) / (max_claim - min_claim)

        base_premium = 1000
        premium = base_premium * (1 + risk_score) * 1.2  # For including the profit margin

        return jsonify({
            'predicted_claim_amount': round(prediction, 2),
            'risk_score': round(risk_score, 4),
            'recommended_premium': round(premium, 2)
        })
    except Exception as e:
        print(f"API Error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)