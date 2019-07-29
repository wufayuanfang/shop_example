import pickle

from com.ly16.domain.User import User
from com.ly16.util.net_util import connect_shop_server


def add_user(user):  # 向服务器添加用户请求
    # 链接总部服务器验证管理员
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("user_oper", "add_user", user)))
    
    result = pickle.loads(clientSocket.recv(1024))  # 获得结果
    clientSocket.close()  # 使用后一定要关闭连接
    
    return result  # 返回结果


def remove_user(user_id):
    clientSocket = connect_shop_server()
    user = User(user_id, "1是假参数，不起作用", "1", "1", "1")
    clientSocket.send(pickle.dumps(("user_oper", "remove_user", user)))
    
    result = pickle.loads(clientSocket.recv(1024))
    clientSocket.close()  # 使用后一定要关闭连接
        
    return  result


def update_user(user):
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("user_oper", "update_user", user)))
    
    result = pickle.loads(clientSocket.recv(1024))
    clientSocket.close()  # 使用后一定要关闭连接
        
    return  result


def select_user(user_id):
    clientSocket = connect_shop_server()
    user = User(user_id, "1是假参数，不起作用", "1", "1", "1")
    clientSocket.send(pickle.dumps(("user_oper", "select_user", user)))
    
    result , user = pickle.loads(clientSocket.recv(1024))
    clientSocket.close()  # 使用后一定要关闭连接
        
    return  result, user


def get_all_user():
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("user_oper", "get_all_user")))
    
    users = pickle.loads(clientSocket.recv(1024 * 3))  # 获取全部用户应大一点
    clientSocket.close()  # 使用后一定要关闭连接
        
    return  users


def select_new_user():  # 向服务器查询最新注册的一个用户数据
    
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("user_oper", "select_new_user")))
    
    user = pickle.loads(clientSocket.recv(1024))
    clientSocket.close()  # 使用后一定要关闭连接
        
    return  user


def net_validate_admin_user(user):
    # 链接总部服务器验证管理员
    clientSocket = connect_shop_server()
    clientSocket.send(pickle.dumps(("user_oper", "net_validate_admin_user", user)))
    
    login_stat, user = pickle.loads(clientSocket.recv(1024))
    clientSocket.close()  # 使用后一定要关闭连接
    
    is_admin = 'N'
    if login_stat:
        is_admin = user.is_admin
        
    return login_stat, is_admin
