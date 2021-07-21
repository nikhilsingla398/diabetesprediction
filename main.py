import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
from flask_cors import cross_origin
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

ss=StandardScaler()

app = Flask(__name__)
model = pickle.load(open("diabetes_predict.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Pregnancies=int(request.form['Pregnancies'])
       
        #Pregnancies2=ss.fit_transform(Pregnancies)
   
        Glucose=int(request.form['Glucose'])
        
        #Glucose2=ss.fit_transform(Glucose)
        
        BloodPressure=int(request.form['BloodPressure'])
        
        #BloodPressure2=ss.fit_transform(BloodPressure)
        
        SkinThickness=int(request.form['SkinThickness'])
        
        #SkinThickness2=ss.fit_transform(SkinThickness)
        
        Insulin=int(request.form['Insulin'])
        
        #Insulin2=ss.fit_transform(Insulin)
       
        BMI=float(request.form['BMI'])
        
        #BMI2=ss.fit_transform(BMI)
        
        DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
        
        #DiabetesPedigreeFunction2=ss.fit_transform(DiabetesPedigreeFunction)
       
        Age=int(request.form['Age'])
        
        #Age2=ss.fit_transform(Age)
        
        data=np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        prediction=model.predict(data)
        
        if(prediction==1):
            return render_template('index.html',prediction_text='sorry!!! you are suffering from diabetes,take imidiate action')
        else:
            return render_template('index.html',prediction_text='congo!! you can eat sweets,you are not suffering from diabetes')
    
    return render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True)