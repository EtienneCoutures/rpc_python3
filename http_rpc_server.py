from flask import Flask, Response, make_response, json, jsonify
from flask_jsonrpc import JSONRPC
from dicttoxml import dicttoxml
import time
import psutil
app = Flask(__name__)

jsonrpc = JSONRPC(app, '/')

@jsonrpc.method('add')
def get_add(a, b):
        resp = make_response(json.dumps({'value': a + b}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp 

@jsonrpc.method('isConnected')
def isConnected():
    return true

@jsonrpc.method('sub')
def get_sub(a, b):
        resp = make_response(json.dumps({'value': a - b}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp 

@jsonrpc.method('json_to_xml')
def get_json_to_xml(string):
        xml = dicttoxml.dicttoxml(json.loads(string))
        resp = make_response(json.dumps({'value': str(xml)}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp

@jsonrpc.method('time')
def get_time():
        resp = make_response(json.dumps({'time': int(time.time())}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp 

@jsonrpc.method('ram')
def get_ram():
        total = psutil.virtual_memory().total / 1024 / 1024
        used = psutil.virtual_memory().used / 1024 / 1024
        resp = make_response(json.dumps({'total': total, 'used': used}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp 

@jsonrpc.method('hdd')
def get_hdd():
        total = psutil.disk_usage('/').total / 1024 / 1024
        used = psutil.disk_usage('/').used / 1024 / 1024
        resp = make_response(json.dumps({'total': total, 'used': used}), 200)
        resp.headers['Content-type'] = 'application/json'
        return resp 

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000)
