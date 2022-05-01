# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import data_tools as dt
import json
from tqdm import tqdm

app = Flask(__name__)

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'tyang'
    password = '8269264ty'
    database = 'codedb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@180.76.168.236:5432/%s' % (user,password,database)

    # 设置sqlalchemy自动更跟踪数据库
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = False

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role') # 反推与role关联的多个User模型对象

    def __init__(self, name):
        self.name = name


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    intro = db.Column(db.Text)
    locate = db.Column(db.String(64))
    school = db.Column(db.String(64))
    avatar = db.Column(db.Text)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id',ondelete='SET NULL')) # 设置外键

    def __init__(self, name, password, sex, intro, locate, school, role_id):
        self.name = name
        self.password = password
        self.sex = sex
        self.intro = intro
        self.locate = locate
        self.school = school
        # self.role_id = role_id

    def dict(self):
        return {
            "name": self.name, "sex": self.sex,
            "intro": self.intro, "locate": self.locate, "school": self.school,
            "avatar": self.avatar
        }

class Repository(db.Model):
    __tablename__ = 'repository'
    
    id = db.Column(db.Integer, primary_key=True)
    # 仓库名称
    name = db.Column(db.String(128))
    path = db.Column(db.String(512), unique=True)
    url = db.Column(db.String(512))
    finished = db.Column(db.Boolean, default=False)
    
    def __init__(self, id_, name, path, url, finished):
        self.id = id_
        self.name = name
        self.path = path
        self.url = url
        self.finished = finished
        


class SourceDir(db.Model):
    """
    源代码目录，一般对应 : src/main/java/...
    """
    __tablename__ = 'sourcedir'

    id = db.Column(db.Integer, primary_key=True)
    repository_id = db.Column(db.Integer, db.ForeignKey('repository.id',ondelete='CASCADE'))
    path = db.Column(db.String(512), unique=True)
    
    def __init__(self, id_, repository_id, path):
        self.id = id_
        self.repository_id = repository_id
        self.path = path


class Package(db.Model):
    __tablename__ = 'package'
    
    id = db.Column(db.Integer, primary_key=True)
    source_dir_id = db.Column(db.Integer, db.ForeignKey('sourcedir.id',ondelete='CASCADE'))
    name = db.Column(db.String(512))
    path = db.Column(db.String(512), unique=True)
    
    def __init__(self, id_, source_dir_id, name, path):
        self.id = id_
        self.source_dir_id = source_dir_id
        self.name = name
        self.path = path
        

class Java(db.Model):
    __tablename__ = 'java'
    
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id',ondelete='CASCADE'))
    name = db.Column(db.String(512))
    path = db.Column(db.String(512), unique=True)
    xml = db.Column(db.String(512), nullable=True)
    
    def __init__(self, id_, package_id, name, path, xml):
        self.id = id_
        self.package_id = package_id
        self.name = name
        self.path = path
        self.xml = xml


class Clazz(db.Model):
    __tablename__ = 'clazz'
    
    id = db.Column(db.Integer, primary_key=True)
    java_id = db.Column(db.Integer, db.ForeignKey('java.id',ondelete='CASCADE'))
    name = db.Column(db.String(128))
    tpe = db.Column(db.String(128), nullable=True)
    signature = db.Column(db.Text, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    
    def __init__(self, id_, java_id, name, tpe, signature, comment):
        self.id = id_
        self.java_id = java_id
        self.name = name
        self.tpe = tpe
        self.signature = signature
        self.comment = comment


class Import(db.Model):
    __tablename__ = 'import'
    
    id = db.Column(db.Integer, primary_key=True)
    java_id = db.Column(db.Integer, db.ForeignKey('java.id',ondelete='CASCADE'))
    import_clazz_id = db.Column(db.Integer, db.ForeignKey('clazz.id',ondelete='CASCADE'))
    
    def __init__(self, id_, java_id, import_clazz_id):
        self.id = id_
        self.java_id = java_id
        self.import_clazz_id = import_clazz_id


class Inherit(db.Model):
    __tablename__ = 'inherit'

    id = db.Column(db.Integer, primary_key=True)
    super_clazz_id = db.Column(db.Integer, db.ForeignKey('clazz.id',ondelete='CASCADE'))
    sub_clazz_id = db.Column(db.Integer, db.ForeignKey('clazz.id',ondelete='CASCADE'))
    
    def __init__(self, id_, super_clazz_id, sub_clazz_id):
        self.id = id_
        self.super_clazz_id = super_clazz_id
        self.sub_clazz_id = sub_clazz_id


class Attribute(db.Model):
    __tablename__ = 'attribute'

    id = db.Column(db.Integer, primary_key=True)
    clazz_id = db.Column(db.Integer, db.ForeignKey('clazz.id',ondelete='CASCADE'))
    tpe = db.Column(db.String(128))
    name = db.Column(db.String(128))
    
    def __init__(self, id_, clazz_id, tpe, name):
        self.id = id_
        self.clazz_id = clazz_id
        self.tpe = tpe
        self.name = name


class Method(db.Model):
    __tablename__ = 'method'

    id = db.Column(db.Integer, primary_key=True)
    clazz_id = db.Column(db.Integer, db.ForeignKey('clazz.id',ondelete='CASCADE'))
    name = db.Column(db.String(256), nullable=True)
    tag = db.Column(db.String(16))
    signature = db.Column(db.Text, nullable=True)
    tpe = db.Column(db.String(256), nullable=True)
    arg_num = db.Column(db.Integer)
    content = db.Column(db.Text, nullable=True)
    doc = db.Column(db.Text, nullable=True)
    
    def __init__(self, id_, clazz_id, name, tag, signature, tpe, arg_num, content, doc):
        self.id = id_
        self.clazz_id = clazz_id
        self.name = name
        self.tag = tag
        self.signature = signature
        self.tpe = tpe
        self.arg_num = arg_num
        self.content = content
        self.doc = doc


class Call(db.Model):
    __tablename__ = 'call'

    id = db.Column(db.Integer, primary_key=True)
    callee_id = db.Column(db.Integer, db.ForeignKey('method.id',ondelete='CASCADE'))
    called_id = db.Column(db.Integer, db.ForeignKey('method.id',ondelete='CASCADE'))
    statement = db.Column(db.Text, nullable=True)
    
    def __init__(self, id_, callee_id, called_id, statement):
        self.id = id_
        self.callee_id = callee_id
        self.called_id = called_id
        self.statement = statement
        

class Override(db.Model):
    """
    覆盖关系
    """
    __tablename__ = 'override'

    id = db.Column(db.Integer, primary_key=True)
    source_method_id = db.Column(db.Integer, db.ForeignKey('method.id',ondelete='CASCADE'))
    rewrite_method_id = db.Column(db.Integer, db.ForeignKey('method.id',ondelete='CASCADE'))
    
    def __init__(self, id_, source_method_id, rewrite_method_id):
        self.id = id_
        self.source_method_id = source_method_id
        self.rewrite_method_id = rewrite_method_id
        

class Base(db.Model):
    __tablename__ = 'base'

    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.Text)
    summary = db.Column(db.Text)
    method_token = db.Column(db.Text)
    summary_token = db.Column(db.Text)

    def __init__(self, id_, method, summary, method_token, summary_token):
        self.id = id_
        self.method = method
        self.summary = summary
        self.method_token = method_token
        self.summary_token = summary_token

class Class2Base(db.Model):
    __tablename__ = 'class2base'

    id = db.Column(db.Integer, primary_key=True)
    base_id = db.Column(db.Integer, db.ForeignKey('base.id',ondelete='CASCADE'))
    method = db.Column(db.Text)
    method_token = db.Column(db.Text)

    def __init__(self, base_id, method, method_token):
        self.id = id_
        self.base_id = base_id
        self.method = method
        self.method_token = method_token


def migrate_repository():
    with open('./data/all/repository.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        repository = Repository(n_line['id'], n_line['name'], n_line['path'],
                                n_line['url'], n_line['finished'])
        db.session.add(repository)
        db.session.commit()

def migrate_sourcedir():
    with open('./data/all/sourcedir.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        sourceDir = SourceDir(n_line['id'], n_line['repository_id'], n_line['path'])
        db.session.add(sourceDir)
        db.session.commit()


def migrate_package():
    with open('./data/all/package.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        package = Package(n_line['id'], n_line['source_dir_id'], n_line['name'], n_line['path'])
        db.session.add(package)
        db.session.commit()


def migrate_java():
    with open('./data/all/java.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        java = Java(n_line['id'], n_line['package_id'], n_line['name'], n_line['path'], n_line['xml'])
        db.session.add(java)
        db.session.commit()

def migrate_import():
    with open('./data/all/import.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        import_ = Import(n_line['id'], n_line['java_id'], n_line['import_clazz_id'])
        db.session.add(import_)
        db.session.commit()


def migrate_clazz():
    with open('./data/all/clazz.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        clazz = Clazz(n_line['id'], n_line['java_id'], n_line['name'], 
                      n_line['tpe'], n_line['signature'], n_line['comment'])
        db.session.add(clazz)
        db.session.commit()

def migrate_inherit():
    with open('./data/all/inherit.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        print(n_line)
        
        query_inherit = Inherit.query.filter_by(id=n_line['id']).first()
        if query_inherit:
            continue
        inherit = Inherit(n_line['id'], n_line['super_clazz_id'], n_line['sub_clazz_id'])
        
        db.session.add(inherit)
        db.session.commit()
        
        


def migrate_method():
    with open('./data/all/method.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in tqdm(lines):
        n_line = json.loads(line)
        query_method = Method.query.filter_by(id=n_line['id']).first()
        if query_method:
            continue
        method = Method(n_line['id'], n_line['clazz_id'], n_line['name'], n_line['tag'],
                        n_line['signature'], n_line['tpe'], n_line['arg_num'], n_line['content'],
                        n_line['doc'])
        db.session.add(method)
        db.session.commit()


if __name__ == '__main__':
    # # 删除所有表
    # db.drop_all()
    # # 创建所有表
    # db.create_all()
    
    # admin_role = Role('超级管理员')
    # guest_role = Role('普通用户')
    # db.session.add(admin_role)
    # db.session.add(guest_role)
    # db.session.commit()

    # admin = User('admin', 'admin', 1, '无话可说', '中国/上海/徐汇', '华东理工大学', 1)
    # guest = User('user', 'user', 1, '无话可说', '中国/上海/徐汇', '华东理工大学', 2)
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()

    # base_method = dt.load_base('data/base.json', key='method', is_json=True)
    # base_summry = dt.load_base('data/base.json', key='summary', is_json=True)
    # class_method = dt.load_class('data/class.json', key='class_methods')
    
    # base_method_token = dt.tokenize_code(base_method)
    # base_summry_token = dt.tokenize_code(base_summry)
    # class_method_token = [dt.tokenize_code(c) for c in class_method]
    
    # for i in range(len(base_method)):
    #     base = Base(base_method[i], base_summry[i], str(base_method_token[i]), str(base_summry_token[i]))
    #     db.session.add(base)
    #     db.session.commit()
    #     for j in range(len(class_method[i])):
    #         class2base = Class2Base(i+1, class_method[i][j], str(class_method_token[i][j]))
    #         db.session.add(class2base)
    #         db.session.commit()
    migrate_method()