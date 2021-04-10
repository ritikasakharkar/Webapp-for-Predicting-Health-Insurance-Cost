import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    if features[1] == 'female':
        features[1] = 1
    elif features[1] == 'male':
        features[1] = 0
    if features[4] == 'yes':
        features[4] = 1
    elif features[4] == 'no':
        features[4] = 0
    int_features = [int(x) for x in features]
    int_features[2] = int_features[1] + int_features[2] + int_features[4]
    int_features = [int_features[0],int_features[2],int_features[3]]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Health Insurance Cost will be {}'.format(output*10))


if __name__ == "__main__":
    app.run(debug=True)