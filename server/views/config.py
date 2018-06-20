# coding:utf8
from redis import Redis
# 是否开启flask的调试
# 开启debug调试，会reload2次代码
DEBUG = False

# 监听的端口号
PORT = 5000

# 主页地址
MAIN_URL = 'https://abc.wxapp.nmxxy.cn/'

APP_ID = 'wx4817d      8c71'

APP_SECRET = '0437ee3f80d4f3         38b48597a1'

TOKEN = 'qbtest'

SECRET_KEY = 'pak       gggg'



# PERMANENT_SESSION_LIFETIME = 7200
PERMANENT_SESSION_LIFETIME = 1.5 * 60