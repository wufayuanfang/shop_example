# 目前实现的方法不建立购物车对象，所以此类目前没用到
class CartItem(object):
    def __init__(self, pro_id, buy_num):
        self.pro_id = pro_id
        self.buy_num = buy_num

    def show_cart_item(self):
        print("商品编号：" + str(self.pro_id), "购买数量：" + str(self.buy_num))
