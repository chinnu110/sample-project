from __future__ import print_function
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/get-weather', methods=['POST'])
def get_weather():

    zipCode = request.form['zipcode']
    apiKey = '2aa22bfd4f125e1fe25e5f74afdeec7b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    d = "{}?zip={}&APPID={}&units=imperial".format(url, zipCode, apiKey)

    resp = requests.get(d)

    data = resp.json()

    if str(resp.status_code) == '200':

        return render_template('weather.html', response=data)
    else:
        if 'message' in data:
            msg = "<h4>ZIP: {} <br>RESP: {}</h4>".format(zipCode,
                                                         data['message'])
            return msg
        else:
            return str(data)

@app.route('/')
def index():
    # Render index page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
