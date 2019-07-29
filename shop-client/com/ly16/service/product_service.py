import pickle

from com.ly16.util.net_util import connect_shop_server
from com.ly16.domain.Product import Product


def add_product(product):
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "add_product", product)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 获得结果（bool）
    clientSocket.close()  #使用后一定要关闭连接
    
    return result  # 返回添加结果


def remove_product(pro_id):
    # 向服务器发送请求
    # 链接总部服务器验证管理员
    product = Product(pro_id, 1, 1, 1)
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "remove_product", product)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 获得结果
    clientSocket.close()  #使用后一定要关闭连接
    
    return result  # 返回删除商品结果


def update_product(product):
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "update_product", product)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 获得结果（bool）
    clientSocket.close()  #使用后一定要关闭连接
    
    return result  # 返回更新结果


def select_product(pro_id):
    product = Product(pro_id, 1, 1, 1)
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "select_product", product)))
    
    result, product = pickle.loads(clientSocket.recv(1024))  # 获得结果（bool，product）
    clientSocket.close()  #使用后一定要关闭连接
    
    return result, product  # 返回查询到的商品数据


def get_all_pros():
    # 1.用户验证()
    # 2.权限认证，鉴权
    # 数据稽核（证据保留），写日志
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "get_all_pros")))
    
    products = pickle.loads(clientSocket.recv(1024 * 3))  # 获取全部商品应大一点
    clientSocket.close()  #使用后一定要关闭连接
        
    return  products


def select_new_pro():
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("product_oper", "select_new_pro")))
    
    product = pickle.loads(clientSocket.recv(1024))  # 获取全部商品应大一点
    clientSocket.close()  #使用后一定要关闭连接
        
    return  product

