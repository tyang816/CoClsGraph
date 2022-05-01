# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from db import *
import json
import pandas as pd
import os

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


@app.route("/relateshow", methods=["POST"])
def relateshow():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        nodes = []
        links = []
        categories = [{"name": "repository"}, {"name": "sourcedir"}, {"name": "package"}, {"name": "java"},
                       {"name": "class"}, {"name": "import"}, {"name": "inherit"}, {"name": "method"}]
        rep_id = data['rep_id']
        
        rep = Repository.query.filter_by(id=rep_id).first()
        nodes.append({"id": 0, "name":rep.name, "value": 5, "category": 1})
        srcdir = SourceDir.query.filter_by(repository_id=rep_id).limit(5).all()
        srcdir_idx = 1
        pkgs = []
        for src in srcdir:
            nodes.append({"id": srcdir_idx, "name": src.path, "value": 1, "category": 2})
            links.append({"source": 0,"target": srcdir_idx})
            srcdir_idx = srcdir_idx + 1
            pkg = Package.query.filter_by(source_dir_id=src.id).limit(3).all()
            for p in pkg:
                pkgs.append(p)
            
        pkg_idx = srcdir_idx
        javas = []
        for i in range(len(pkgs)):
            nodes.append({"id": pkg_idx, "name": pkgs[i].name, "value": 1, "category": 3})
            links.append({"source": 2+int(i/3),"target": pkg_idx})
            pkg_idx = pkg_idx + 1
            java = Java.query.filter_by(package_id=pkgs[i].id).limit(2).all()
            for j in java:
                javas.append(j)
        
        java_idx = pkg_idx
        clazzs = []
        for i in range(len(javas)):
            nodes.append({"id": java_idx, "name": javas[i].name, "value": 1, "category": 4})
            links.append({"source": srcdir_idx+int(i/2),"target": java_idx})
            java_idx = java_idx + 1
            clazz = Clazz.query.filter_by(java_id=javas[i].id).limit(1).all()
            for c in clazz:
                clazzs.append(c)
        
        clazz_idx = java_idx
        imports = []
        inherits = []
        methods = []
        for i in range(len(clazzs)):
            nodes.append({"id": clazz_idx, "name": clazzs[i].name, "value": 1, "category": 5})
            links.append({"source": pkg_idx + i,"target": clazz_idx})
            clazz_idx = clazz_idx + 1
            import_ = Import.query.filter_by(import_clazz_id=clazzs[i].id).limit(2).all()
            for im in import_:
                imports.append(im)
            inherit = Inherit.query.filter_by(super_clazz_id=clazzs[i].id).limit(2).all()
            for inh in inherit:
                inherits.append(inh)
            method = Method.query.filter_by(clazz_id=clazzs[i].id).limit(2).all()
            for m in method:
                methods.append(m)
                
        import_idx = clazz_idx
        for i in range(len(imports)):
            nodes.append({"id": import_idx, "name": imports[i].import_clazz_id, "value": 1, "category": 7})
            links.append({"source": java_idx + int(i/2),"target": import_idx})
            import_idx = import_idx + 1
        
        inherit_idx = import_idx
        for i in range(len(inherits)):
            nodes.append({"id": inherit_idx, "name": inherits[i].super_clazz_id, "value": 1, "category": 8})
            links.append({"source": java_idx + int(i/2),"target": inherit_idx})
            inherit_idx = inherit_idx + 1
        
        method_idx = inherit_idx
        for i in range(len(methods)):
            nodes.append({"id": method_idx, "name": methods[i].signature, "value": 1, "category": 9})
            links.append({"source": java_idx + int(i/2),"target": method_idx})
            method_idx = method_idx + 1
        
        res = {"code": "200", "type": "force", "categories": categories,
               "nodes": nodes, "links": links}
        
    return jsonify(res)

@app.route("/jielong", methods=["POST"])
def jielong():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        lines = data['content'].split('\n')
        clazz = data['clazz']
        
        names = []
        for line in lines:
            name = line.split()[1]
            if name not in names:
                names.append(name)

        df = pd.read_excel('./data/信息学院18级在校学生名单.xlsx'+total_xlsx[0])
        names_all = df[df['班级'].isin([clazz])]['姓名'].tolist()
        not_jielong = set(names_all) - set(names)
        
        ans1 = ""
        ans2 = ""
        for name in list(not_jielong):
            tel = df[df['姓名'].isin([name])]['电话'].tolist()[0]
            ans1 = ans1 + "@" + name + " "
            ans2 = ans2 + str(list(not_jielong).index(name)+1) + '.' + name + "未回复+%s"%tel + '\n'

        res = {
            "code": "200", "ans1": ans1, "ans2": ans2
        }
    return jsonify(res)

@app.route("/jielong5", methods=["POST"])
def jielong5():
    res = {"code":"500"}
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        lines = data['content'].split('\n')
        rooms = []
        for line in lines:
            room = line.split()[1][:3]
            if room not in rooms:
                rooms.append(room)
        df = pd.read_excel('./data/23舍5层核酸分组.xlsx')
        rooms_list = df['宿舍'].tolist()
        rooms_all = []
        for room in rooms_list:
            rooms_all.append(room[7:])
        not_jielong = set(rooms_all) - set(rooms)
        
        ans1 = ""
        for room in list(not_jielong):
            ans1 = ans1 + room + " "

        res = {
            "code": "200", "ans1": ans1
        }
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
