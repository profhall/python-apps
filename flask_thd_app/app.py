"""
title: app
author: Phillip Hall
date: 2019-10-03 09:16
working example: ompyapp.apps-np.homedepot.com
"""

from flask import Flask, render_template
from api_get_token import API_Handle
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/markets')
def markets():
    markets_url = 'https://master-data-location.apps-np.homedepot.com/location/markets'

    response = API.get_data(markets_url)
    json_response = response.json()
    return (json_response) #will return object
    # return (json.dumps(json_response, indent=4)) #will return string rep of object

@app.route('/template/markets')
def markets_template():
    markets_url = 'https://master-data-location.apps-np.homedepot.com/location/markets'

    response = API.get_data(markets_url)
    json_response = response.json()
    # return (json_response) #will return object
    user = {'username': 'Homer'}
    return render_template('markets.html', title='THD Markets', user=user)




if __name__ == '__main__':
    API = API_Handle()
    port = int(os.getenv('PORT', '8000'))  # set to server environment defualt port if exist set other choose port 3000
    app.run(host='0.0.0.0', port=port, debug=True)