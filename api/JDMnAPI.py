#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime, timedelta
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
from json import dumps
from requests import post

import hashlib
import JDMn
import os
import time
import uuid

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*","methods":"POST,DELETE,PUT,GET,OPTIONS"}})

def evaluateJDMn(content):
    bodyTable     = content     ['JDMn'          ]
    definitions   = bodyTable   ['definitions'   ]
    decision      = definitions ['decision'      ]
    decisionTable = decision    ['decisionTable' ]
    condition     = content     ['condition'     ]
    
    dataResult = {}
    result, prove = JDMn.evaluateJDMn(decisionTable, condition, 'S')
    
    dataResult['result'] = result
    dataResult['prove' ] = prove
    
    return dataResult

@app.route('/jdmn', methods=['GET'])
def decompoe():
    reg = {}
    
    if request.json == None:
        return jsonify( { 'error': 'No parameters found.' } )
    else:
        if 'evaluate' in request.json:
            if 'evaluate' in request.json:
                reg['_id'] =  str(uuid.uuid4())
                start_time_millis = int(time.time() * 1000)
                reg['evaluate'] = evaluateJDMn(request.json['evaluate'])
                end_time_millis = int(time.time() * 1000)
                reg['processing time'] = str(end_time_millis - start_time_millis) + ' ms'
                print(reg['_id'] + ' - ' + reg['processing time'])
        else:
            return jsonify( { 'error': 'No keys valid found.' } )
    
    json_result = reg
    return jsonify(json_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '8080'))