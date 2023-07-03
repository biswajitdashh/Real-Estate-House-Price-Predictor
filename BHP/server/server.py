from flask import Flask, request, jsonify, redirect, url_for
import util

app= Flask(__name__)

@app.route('/get_location_names', methods=['GET','POST'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Allow-Control-Origin','*')
    return response

@app.route('/predict_home_price',methods = ['POST','GET'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({'estimated_price': util.get_price(location, total_sqft, bhk, bath)})
    return response

@app.route('/')
def index():
    return 'Starting Python Flask Server for home price prediction'

if __name__ == '__main__':
    app.run()

