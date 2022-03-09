from flask import Flask, request, jsonify
from db import User, Role
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
        print(user)
    return jsonify(res)




@app.route("/comment", methods=['POST'])
def comment():
    
    return 


if __name__ == "__main__":
    app.run(debug=True)