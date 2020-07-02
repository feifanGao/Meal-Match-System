import sys
from flask_cors import CORS
from json import dumps
from flask import Flask,request

APP = Flask(__name__)
CORS(APP)

import func.data
from func.sys import *
#sys fuctions
@APP.route('/sys/register',methods = ['POST'])
def register():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    result = sys_register(email,username,password)
    return dumps(result)

@APP.route('/sys/login',methods = ["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    result = sys_login(email,password)
    return dumps(result)

@APP.route('/sys/logout',methods = ["POST"])
def logout():
    token = request.form.get("token")
    result = sys_logout(token)
    return dumps(result)

if __name__ == '__main__':
    APP.run(port = (sys.argv[1] if len(sys.argv) > 1 else 5000))
