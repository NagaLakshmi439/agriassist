from flask import Flask, render_template, request
import numpy as np
import pickle
import os

from utils.chatbot import chatbot_reply
from utils.weather import get_weather
from utils.soil_image import analyze_soil_image
from utils.disease import predict_disease

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ph = float(request.form['ph'])
    n = float(request.form['nitrogen'])
    p = float(request.form['phosphorus'])
    k = float(request.form['potassium'])
    mg = float(request.form['magnesium'])

    data = np.array([[ph, n, p, k, mg]])
    result = model.predict(data)[0]

    return render_template('result.html', result=result)

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.form['message']
    reply = chatbot_reply(msg)
    return render_template('result.html', result=reply)

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    result = get_weather(city)
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
