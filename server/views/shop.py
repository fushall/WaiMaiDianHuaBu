# coding: utf8


from . import app
from models.shop import Shop

from flask import jsonify

@app.route('/shops')
def shops():
    js = jsonify(Shop.get_all())

    file = open('json', 'wb')
    file.write(js.data)
    return js