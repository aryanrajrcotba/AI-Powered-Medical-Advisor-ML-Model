from flask import Flask, render_template, request
from model import predict_disease
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction, solution = None, None
    
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        prediction, solution = predict_disease(symptoms)
    
    return render_template('as.html', prediction=prediction, solution=solution)

if __name__ == '__main__':
    app.run(debug=True)