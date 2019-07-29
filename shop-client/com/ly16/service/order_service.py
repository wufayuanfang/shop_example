import pickle

from com.ly16.domain.Order import Order
from com.ly16.util.net_util import connect_shop_server


def add_order(order_new):  # 添加订单
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "add_order", order_new)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 添加订单请求
    
    clientSocket.close()  #使用后一定要关闭连接
        
    return  result


def get_all_order():  # 获得所有订单
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "get_all_order")))
    
    orders = pickle.loads(clientSocket.recv(1024 * 3))  # 获取全部订单应大一点
    
    clientSocket.close()  #使用后一定要关闭连接

        
    return  orders


def select_new_order():  # 查找到最新生成的一条订单数据
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "select_new_order")))
    
    order = pickle.loads(clientSocket.recv(1024))  # 查询最新数据请求
    clientSocket.close()  #使用后一定要关闭连接
        
    return  order


def select_order(order_id):  # 查询订单
    
    order = Order(order_id, 1, 1, 1, "这是假数据", "None", None)
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "select_order", order)))
    
    result, order = pickle.loads(clientSocket.recv(1024))  # 添加订单请求
    clientSocket.close()  #使用后一定要关闭连接
        
    return  result, order


def remove_order(order_id):  # 删除订单
    order = Order(order_id, 1, 1, 1, "这是假数据", "None", None)
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "remove_order", order)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 删除订单请求
    clientSocket.close()  #使用后一定要关闭连接
        
    return  result

# def change_order(order):
#     return update_order(order)


def modify_order_stat(order_id, order_new_stat):
    order = Order(order_id, 1, 1, 1, "这是假数据", order_new_stat, None)
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("order_oper", "modify_order_stat", order)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 改变订单状态请求
    clientSocket.close()  #使用后一定要关闭连接
        
    return  result

# change_order(1009, 1000, 1021, 77, "武汉")
