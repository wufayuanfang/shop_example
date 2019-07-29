'''
Created on 2019年7月25日

@author: 卢艺

商品服务器，处理各个分店请求中心控制器
'''

import pickle  # 序列化
import socket  # 套接字
import threading  # 线程模块

from com.ly16.controller.process_common_thread import process_common_requst
from com.ly16.controller.process_order_thread import process_order_requst
from com.ly16.controller.process_product_thread import process_product_requst
from com.ly16.controller.process_user_thread import process_user_requst


def start_shop_server():
    print("神州通联商城总部服务器启动中。。。。")
    # socket.AF_INET:IPv4(128.0.0.1) 
    # socket>SOCK_STREAM:TCP协议 传输可靠 ACK确认信号性能差
    # SOCK__DGRAM:UDP协议 传输不可靠 性能好
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("127.0.0.1", 9999))  # 绑定到IP地址，拒绝私服
    
    serverSocket.listen(20)  # 等待最大的链接数
#     client_num = 0
    while True:
        clientSocket, adr = serverSocket.accept()  # F 等待客户端请求 阻塞函数：客户连接来了就执行，没有连接请求就等待  同步机制
        print("接收到客户端{}请求".format(adr[0]))
#         client_num += 1
        print(adr)
        
        data = pickle.loads(clientSocket.recv(1024))  # 反序列化
        if data[0] == "user_oper":
            # 序列化
            # clientSocket.send(pickle.dumps("不要回答！不要回答！不要回答！"))
            # 处理繁重业务
            
            t = threading.Thread(target=process_user_requst, args=(clientSocket, data,))
            
            # 启动线程，让线程进入可运行状态，等待CPU/GPU调度
            t.start()
            
        if data[0] == "product_oper":
            t = threading.Thread(target=process_product_requst, args=(clientSocket, data,))
            t.start()
            
        if data[0] == "order_oper":
            t = threading.Thread(target=process_order_requst, args=(clientSocket, data,))
            t.start()
            
        if data[0] == "common_oper":
            t = threading.Thread(target=process_common_requst, args=(clientSocket, data,))
            t.start()


if __name__ == '__main__':
    start_shop_server()
