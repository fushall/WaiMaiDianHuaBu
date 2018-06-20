# coding: gbk

from . import db

#sys.setdefaultencoding(utf-8)
def str2bin(strText):
    b = bytes((ord(i) for i in strText))
    return b

#codec can be 'gb2312','utf8' etc
def getCode(strText,codec):
    b = bytes((ord(i) for i in strText))
    return b.decode(codec)



class Shop(db.Model):
    __tablename__ = 'shops'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(10), nullable=False)
    phonenumbers = db.Column(db.Unicode(12*4))
    description = db.Column(db.Unicode(40))
    categories = db.relationship('Category', backref='categories')

    def __repr__(self):
        return '<name:{}, phonenumber:{}, description:{}>'.format(
            self.name, self.phonenumbers, self.description
        )
    def __str__(self):
        return  self.__repr__()

    @classmethod
    def get_all(cls):

        # 把数据库里的所有数据提取成python的数据类型
        shops = []
        for shop in cls.query.all():
            categories_in_one_shop = []
            for category in shop.categories:
                foods_in_one_category = []
                for food in category.foods:
                    foods_in_one_category.append({
                        'name': food.name,
                        'price': food.price,
                        'quantity': food.quantity,
                        'unit': food.unit
                    })
                categories_in_one_shop.append({

                    'name': category.name,
                    'foods': foods_in_one_category
                })
            shops.append({
                'name': shop.name,
                # 去掉空格然后分组
                'phonenumbers': shop.phonenumbers.replace(' ', '').split(','),
                'description': shop.description,
                'categories': categories_in_one_shop
            })
        return shops


class Category(db.Model):
    __tablename__ = 'categories'

    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(10))
    foods = db.relationship('Food', backref='foods')


class Food(db.Model):
    __tablename__ = 'foods'

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(10))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.Unicode(3))

