# coding: utf8

from views import manager,app
from models import db
from models.shop import Shop, Category, Food
from models.user import User

@app.before_first_request
def before_first_request():
	# 生成测试数据
    return 
    db.drop_all()
    db.create_all()
    user = User()
    user.openid = '666'
    db.session.add(user)
    db.session.commit()

    for x in range(10):
        shop = Shop()
        shop.name = '麻辣卡鸭子' + str(x)
        shop.phonenumbers = '1,2,3'
        categories = []
        for y in range(5):
            category = Category()
            category.name = '分类' + str(y)
            foods = []
            for z in range(10):
                food = Food()
                food.name = '食物名称' + str(z)
                food.unit = str(z)
                food.price = str(z)
                food.quantity = str(z)
                foods.append(food)
            category.foods = foods
            categories.append(category)
        shop.categories = categories
        db.session.add(shop)
    db.session.commit()



if __name__ == '__main__':
    print(app.url_map)
    # app.debug = True
    # manager.run()
    app.run()


