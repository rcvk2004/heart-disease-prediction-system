from flask import Flask, render_template, request, url_for
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
model = pickle.load(open('modelFile.pkl', 'rb'))

@app.route('/')
@app.route('/home')
def main():
    return render_template('heartform.html')

@app.route('/result', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    if input_data[5]>120:           # if fbs is >120
        input_data[5] = 1
    else:
        input_data[5] = 0

    input_data = [np.array(input_data)]
    df = pd.DataFrame(input_data, columns=features)
    res = model.predict(df)
    if res==1:
        value = 'high risk'
    else:
        value = 'low risk'

    return render_template('resultpage.html', value=value)