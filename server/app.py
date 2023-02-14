#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/eta', methods=['GET', 'POST'])
def all_res():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        # in_data = request
        in_data = request.get_json()
        path = in_data['path']
        print('in_data:',path)
        # print(type(path)) # list
        response_object['prediction'] = 123
    else:
        response_object['prediction'] = 'INVALID'
    
    return jsonify(response_object)




if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()