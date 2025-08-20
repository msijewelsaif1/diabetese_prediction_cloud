from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('diabetes_prediction_model.joblib')

# Define the route for the main page
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get the input values from the form
        glucose = float(request.form['glucose'])
        bmi = float(request.form['bmi'])
        insulin = float(request.form['insulin'])
        age = float(request.form['age'])

        # Prepare the input array for prediction
        input_data = np.array([[glucose, bmi, insulin, age]])

        # Make the prediction using the model
        prediction_result = model.predict(input_data)
        
        # Convert prediction to readable output
        prediction = "Diabetic" if prediction_result[0] == 1 else "Not Diabetic"

    return render_template('index.html', prediction=prediction)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
