from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('DecisionTreeClassifier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        SoilMoisture = float(request.form['SoilMoisture'])
        Temperature = float(request.form['Temperature'])
        Humidity = int(request.form['Humidity'])
        
        prediction=model.predict([[Temperature,Humidity,SoilMoisture]])
        output=prediction[0]
        if output==0:
            return render_template('index.html',prediction_text="Turn off the Motor")
        else if output>0:
            return render_template('index.html',prediction_text="Turn on the Motor")   
        else:
            return render_template('index.html',prediction_text="Turn on the Motor".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
