#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from flask import Flask, jsonify, request
from flask_cors import CORS
from eta import eta

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
        response_object['prediction'] = eta(path, 1374232948)
    else:
        response_object['prediction'] = 'INVALID'
    
    return jsonify(response_object)




if __name__ == '__main__':
    print(os.getcwd())
    os.chdir('../')
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=False) # debug=True时，会执行两遍前面的代码，很怪。详见http://www.codebaoku.com/question/question-sd-1010000007344236.html

