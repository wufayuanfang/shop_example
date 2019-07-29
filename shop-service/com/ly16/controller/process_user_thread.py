'''
Created on 2019年7月25日

@author: 卢艺
'''
import pickle

from com.ly16.service.user_service import validate_admin_user, add_user, \
    select_new_user, update_user, remove_user, select_user, get_all_user


def process_user_requst(clientSocket, data):
    print("user线程体")
    
    if data[1] == "net_validate_admin_user":
        # 验证用户账户和密码
       
        is_validate_success, user = validate_admin_user(data[2].user_id, data[2].password)
        
        clientSocket.send(pickle.dumps((is_validate_success, user)))
        clientSocket.close()  #使用后一定要关闭连接
        return
            
    if data[1] == "add_user":
        # 添加一个用户
        result = add_user(data[2])  # 获得添加结果
        
        clientSocket.send(pickle.dumps((result)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
        
    if data[1] == "select_new_user":
        # 查找最新添加的用户数据
        user = select_new_user()  # 获得最新添加的用户数据
        
        clientSocket.send(pickle.dumps((user)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "update_user":
        # 更新用户信息
        result = update_user(data[2])  # 获得更新结果
        
        clientSocket.send(pickle.dumps((result)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "remove_user":
        # 删除用户
        result = remove_user(data[2].user_id)  # 获得删除结果
        
        clientSocket.send(pickle.dumps((result)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "select_user":
        # 查找一个用户，
        result , user = select_user(data[2].user_id)  # 获得删除结果
        
        clientSocket.send(pickle.dumps((result, user)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "get_all_user":
        # 查找所有用户，
        users = get_all_user()  # 获得所有用户信息
        
        clientSocket.send(pickle.dumps((users)))  # 向客户端返回数据
        clientSocket.close()  #使用后一定要关闭连接
        return
