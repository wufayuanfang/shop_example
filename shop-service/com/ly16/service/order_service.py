from com.ly16.dao.order_dao import select_all_order, insert_order, select_desc, select_ord, delete_order, update_order, \
    update_order_stat


def add_order(order_new):  # 添加订单
    return insert_order(order_new)


def get_all_order():  # 获得所有订单
    return select_all_order()


def select_new_order():  # 查找到最新生成的一条订单数据
    id = select_desc()  # 查找到数据表最底的一条订单数据的ID

    # 实现时并未考虑到是否直接拿到数据库订单表最底下的一条数据，后续可验证更新

    order_new = select_ord(id)  # 用ID查找到这条数据
    # 返回的是（布尔值，数据）  布尔值是查找是否成功反馈：成True 否False
    return order_new[1]  # 返回的是一个订单数据


def select_order(order_id):  # 查询订单
    return select_ord(order_id)


def remove_order(order_id): #删除订单
    return delete_order(order_id)


def change_order(order):
    return update_order(order)


def modify_order_stat(order_id, order_new_stat):
    return update_order_stat(order_id, order_new_stat)
# change_order(1009, 1000, 1021, 77, "武汉")
