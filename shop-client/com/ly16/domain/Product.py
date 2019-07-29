"""
定义类
"""


# _成员：是受保护的，给子类用  __成员:私有的

class Product(object):
    # 构造函数，构造器,是在创建对象时自动调用
    def __init__(self, pro_id, pro_name, pro_price, pro_num):
        # 成员变量=参数
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.pro_price = pro_price
        self.pro_num = pro_num

    def show_pro(self):
        print("商品编号：" + str(self.pro_id), "商品名称：" + self.pro_name, "价格：" + str(self.pro_price),
              "数量：" + str(self.pro_num))


if __name__ == '__main__':
    pro = Product(1044, "遥控汽车", 98.6, 8000)
    pro.show_pro()
