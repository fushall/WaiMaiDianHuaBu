# coding: utf8

from . import app, api, login_manager
from flask_login import login_user, logout_user, login_required
from flask import session, request, jsonify, redirect
from flask_restful import Resource, reqparse, fields, marshal
from utils import decrypt_encrypted_data, generate_key, sha1
from models.user import db, User, Feedback
import requests


@login_manager.user_loader
def wxuser_loader(user_id):
    return  User.query.get(int(user_id))

class Login(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('js_code', type=str, required=True)
        self.parser = parser

        self.login_fields = {
            'session': fields.String,
            'openid': fields.String
        }

    @staticmethod
    def jscode2session(js_code):
        '''
        小程序中的wx.login 返回的 code 换 session
        :param js_code: wx.login success(res) res.code
        :return: {'session_key':xxx,
                  'expires_in':yyy, 默认两小时
                  'openid':zzz}
        '''

        params = {'appid': app.config['APP_ID'],
                  'secret': app.config['APP_SECRET'],
                  'js_code': js_code,
                  'grant_type': 'authorization_code'
                  }
        response = requests.get('https://api.weixin.qq.com/sns/jscode2session', params=params)
        if response.status_code == requests.codes.ok:
            return response.json()


    def post(self):
        args = self.parser.parse_args()
        resp = self.jscode2session(args['js_code'])
        print(resp)
        if isinstance(resp, dict):
            # 先登出
            logout_user()

            openid = resp.get('openid')
            # 新用户的话则存入数据库
            user = User.get(openid)
            if user is None:
                user = User.add(openid)

            login_user(user)

            session.update({'openid': openid})

            print(session)
        return marshal(session, self.login_fields)

@app.route('/gaga')
@login_required
def gaga():
    return jsonify({'gaga': 'gaga'})

@app.route('/login666')
def login666():
    user = User.get('666')
    if user is None:
        user = User.add('666')
    login_user(user)
    session['openid'] = '666'
    return redirect('/gaga')

@app.route('/addtext')
@login_required
def addtext():
    x = Feedback.add(request.args.get('text'))
    return str(x.text)

@app.route('/notice')
def sss():
    x = Feedback.query.filter_by(user_id=None).order_by(db.desc(Feedback.post_at)).all()
    l = []
    for u in x:
        l.append(str(u.text))
    return str(l)


api.add_resource(Login, '/login/')