from flask import Flask, json
from flask_jsonrpc.proxy import ServiceProxy

class Client:

    def __init__(self, addr):    
        self.server = ServiceProxy("http://" + addr)

    def add(self, a, b):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline")
        if type(a) is not int or type(b) is not int:
            raise Exception("invalid parameter")
        res = self.server.add(a, b)
        return int(res['value'])

    def sub(self, a, b):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline")
        if type(a) is not int or type(b) is not int:
            raise Exception("invalid parameter")
        res = self.server.sub(a, b)
        return res['value']

    def hdd(self):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline")
        res = self.server.hdd()
        a = int(res['total']) 
        b = int(res['used'])
        return {a , b}

    def time(self):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline") 
        res = self.server.time()
        return int(res['time'])

    def ram(self):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline")
        res = self.server.ram()
        return int(res['total']), int(res['used'])

    def json_to_xml(self, string):
        try:
            self.server.isConnected()
        except:
             raise Exception("server offline")
        if type(string) is not str:
            raise Exception("invalid parameter")
        try:
            json_object = json.loads(string)
        except:
            raise Exception("invalid parameter")
        res = self.server.json_to_xml(string)
        return str(res['value'].split('\'')[1])
