'''
Created on 2019年7月25日

@author: 卢艺
'''

  
import socket


# 序列化:把字符串数据转换成字节数据
# 反序列化：把字数据转化成原有类型
# 链接总部服务器
def connect_shop_server():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1", 9999))
    
    return clientSocket
    
#     data = clientSocket.recv(1024)
#     
#     print(pickle.loads(data))  # 2049--->1024(1) 1024(1) 1(1)  影响到网络I/O次数
    

if __name__ == '__main__':
    pass
