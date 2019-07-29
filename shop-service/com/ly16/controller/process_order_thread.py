

'''
Created on 2019年7月25日

@author: 卢艺
'''
import pickle

from com.ly16.service.order_service import get_all_order, add_order, \
    select_new_order, select_order, remove_order, modify_order_stat


def process_order_requst(clientSocket, data):
    print("order线程体")
    if data[1] == "get_all_order":
        # 获取缓存
       
        orders = get_all_order()
        
        clientSocket.send(pickle.dumps((orders)))
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "add_order":
        # 添加订单
       
        result = add_order(data[2])
        
        clientSocket.send(pickle.dumps((result)))
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "select_new_order":
        # 查询最新生成的订单
       
        order = select_new_order()
        
        clientSocket.send(pickle.dumps((order)))
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "select_order":
        # 查询订单
        result, order = select_order(data[2].order_id)  # 返回（bool，product）
        clientSocket.send(pickle.dumps((result, order)))
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "remove_order":
        # 删除订单
       
        result = remove_order(data[2].order_id)
        
        clientSocket.send(pickle.dumps((result)))
        clientSocket.close()  #使用后一定要关闭连接
        return
    if data[1] == "modify_order_stat":
        # 修改订单状态
       
        result = modify_order_stat(data[2].order_id, data[2].order_stat)
        
        clientSocket.send(pickle.dumps((result)))
        clientSocket.close()  #使用后一定要关闭连接
        return

