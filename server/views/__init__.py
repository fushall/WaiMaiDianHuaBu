# coding: utf8


from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager, Server, Shell, prompt_bool

from models import db
from models.shop import Shop, Category, Food
from models.user import User, Feedback

from flask_restful import Api
from flask_login import LoginManager
from . import config
app = Flask(__name__)

# 加载配置文件
import models.config
app.config.from_object(models.config)
app.config.from_object(config)


# create app
login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)
db.init_app(app)
db.app = app # flask_sqlalchemy 的坑 / 已经修复
admin = Admin(app, name='phonebook', template_mode='bootstrap3')
admin.add_view(ModelView(Shop, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Food, db.session))
admin.add_view(ModelView(Feedback, db.session))
admin.add_view(ModelView(User, db.session))
manager = Manager(app)

def make_shell_context():
    return {
        'db': db,
        'app': app
    }

@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to lose all your data.'):
        db.drop_all()

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(
    use_debugger=True, use_reloader=False
))

# 路由
from . import shop, apis