# coding: utf8



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 添加表结构
from . import shop, user


