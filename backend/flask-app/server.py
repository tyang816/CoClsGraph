from flask import Flask, request, jsonify
from db import *
import json


# 跨域支持
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

app = Flask(__name__)
app.after_request(after_request)


@app.route("/login", methods=['POST'])
def login():
    res = {'code':'500'}
    if request.method == 'POST':
        data = request.data.decode()
        name = data['name']
        password = data['password']
        user = User.query.filter_by(name=name, password=password).first()
        if user:
            res = {'msg':'true'}
    return res

@app.route("/token", methods=['POST'])
def token():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        name = data['username']
        password = data['password']
        user = User.query.filter_by(name=name, password=password).first()
        if user:
            res = {
                "code":"200", 
                "data":{
                    "token": "user.Auth", 
                    "userInfo":{"userId": user.id, "userName": user.name, "dashboard": "1",
                                "userSex": user.sex, "userIntro": user.intro, "userLocate": user.locate,
                                "userSchool": user.school, "userAvatar": user.avatar}
                }
            }
    return jsonify(res)




@app.route("/base", methods=['POST'])
def basemethod():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        base_id = data['base_id']
        base  = Base.query.filter_by(id=base_id).first()
        if base:
            res = {
                "code": "200",
                "data": {
                    "method": base.method, "summary": base.summary, 
                    "method_token": base.method_token, "summary_token": base.summary_token
                }
            }

    return jsonify(res)



@app.route("/class2base", methods=['POST'])
def class2base():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        base_id = data['base_id']
        class2base  = Class2Base.query.filter_by(base_id=base_id).all()
        if class2base[0]:
            res = {
                "code": "200",
                "data": [ 
                    {"method": class2base_i.method, "method_token": class2base_i.method_token} for class2base_i in class2base
                ]
            }

    return jsonify(res)



if __name__ == "__main__":
    app.run(debug=True)