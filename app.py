from flask import Flask, request, render_template
import os
import pickle

print(os.getcwd())
path = os.getcwd()


with open('Models/RF_model.pkl', 'rb') as f:
    randomforest = pickle.load(f)

with open('Models/svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)


def get_predictions(Patient Age, sex, Chest pain, Blood pressure, cholestoral,Fasting blood sugar,electrocardiographic results,maximum heart rate achieved,exercise induced angina,depression induced by exercise,slope of the peak exercise,vessels (0-3) colored by flourosopy,thal):
    mylist = [Patient Age, sex, Chest pain, Blood pressure, cholestoral,Fasting blood sugar,electrocardiographic results,maximum heart rate achieved,exercise induced angina,depression induced by exercise,slope of the peak exercise,vessels (0-3) colored by flourosopy,thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'RandomForest':
        #print(req_model)
        return randomforest.predict(vals)[0]

    elif req_model == 'SVM':
        #print(req_model)
        return svm_model.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    Age = request.form['Patient Age']
    sex = request.form['sex']
    CP = request.form['Chest pain']
    BP = request.form['Blood pressure']
    chol = request.form['cholestoral']
    fbs = request.form['Fasting blood sugar']
    ec = request.form['electrocardiographic results']
    mhrt = request.form['maximum heart rate achieved']
    exng = request.form['exercise induced angina']
    dp = request.form['depression induced by exercise']
    slope = request.form['slope of the peak exercise']
    ca = request.form['vessels (0-3) colored by flourosopy']
    thal = request.form['thal']
    req_model = request.form['req_model']

    target = get_predictions(Age,sex,CP,BP,chol,fbs,ec,mhrt,exng,dp,slope,ca,thal)

    if target==1:
        sale_making = 'Patient is having heart disease'
    else:
        sale_making = 'Patient does not have heart disease'

    return render_template('home.html', target = target, sale_making = sale_making)


if __name__ == "__main__":
    app.run(debug=True)
