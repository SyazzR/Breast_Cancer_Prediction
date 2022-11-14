from flask import Flask, render_template, url_for
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

# Bind home function to URL


@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL

# EDITED ASHLEY (MAU ADA RENDER UTK PREDICT.HTML)


@app.route('/secondpage')
def secondpage():
    return render_template('predict.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Put all form entries values in a list
    features = [float(i) for i in request.form.values()]
    print(features)
    # Convert features to array
    array_features = [np.array(features)]
    print(array_features)

    # Predict features
    prediction = model.predict(array_features)
    output = prediction
    print(output)
    # Check the output values and retrive the result with html tag based on the value
    if output == 0:
        return render_template('predict.html',
                               Diagnosis_text='The patient is likely to have Benign Tumor!')
    else:
        return render_template('predict.html',
                               Diagnosis_text='The patient is likely to have Malign Tumor!')


if __name__ == '__main__':
    # Run the application
    app.run()
