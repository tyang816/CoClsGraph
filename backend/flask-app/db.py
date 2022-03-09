from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = '8269264ty'
    database = 'codedb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@180.76.168.236:3306/%s' % (user,password,database)

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
    # 定义表名
    __tablename__ = 'role'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role') # 反推与role关联的多个User模型对象

    def __init__(self, name):
        self.name = name


class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    intro = db.Column(db.Text)
    locate = db.Column(db.String(64))
    school = db.Column(db.String(64))
    avatar = db.Column(db.Text)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id')) # 设置外键

    def __init__(self, name, password, sex, intro, locate, school, role_id):
        self.name = name
        self.password = password
        self.sex = sex
        self.intro = intro
        self.locate = locate
        self.school = school

    def dict(self):
        return {
            "name": self.name, "sex": self.sex,
            "intro": self.intro, "locate": self.locate, "school": self.school,
            "avatar": self.avatar
        }

class Repository(db.Model):
    # 定义表名
    __tablename__ = 'repository'
    # 定义字段
    


if __name__ == '__main__':
    # 删除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
    admin_role = Role('超级管理员')
    guest_role = Role('普通用户')
    admin = User('admin', 'admin', 1, '无话可说', '中国/上海/徐汇', '华东理工大学', 1)
    guest = User('user', 'user', 1, '无话可说', '中国/上海/徐汇', '华东理工大学', 0)
    db.session.add(admin_role)
    db.session.add(guest_role)
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
