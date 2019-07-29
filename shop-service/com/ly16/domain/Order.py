class Order(object):
    def __init__(self, order_id, user_id, pro_id, buy_num, address, *order_stat):
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.buy_num = buy_num
        self.address = address
        self.order_stat = order_stat[0]
        self.order_time = order_stat[1]

    def decode_order_stat(self, stat):
        if stat == "A":
            return "新订单"
        elif stat == "B":
            return "配货中"
        elif stat == "C":
            return "物流中"
        elif stat == "D":
            return "已签收"
        elif stat == "E":
            return "可归档"
        else:
            return "异常订单"

    def show_order(self):
        print("订单编号：" + str(self.order_id), "用户编号：" + str(self.user_id), "商品编号：" + str(self.pro_id),
              "购买数量:" + str(self.buy_num), "收货地址：" + self.address, "订单状态：" + self.decode_order_stat(self.order_stat),"订单时间："+str(self.order_time))
