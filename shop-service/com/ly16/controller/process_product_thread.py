'''
Created on 2019年7月25日

@author: 卢艺
'''
import pickle

from com.ly16.service.product_service import remove_product, get_all_pros, \
    select_product, update_product, add_product, select_new_pro


def process_product_requst(clientSocket, data):
    print("product线程体")
    if data[1] == "remove_product":
        # 验证用户账户和密码
       
        result = remove_product(data[2].pro_id)
        
        clientSocket.send(pickle.dumps((result)))
        return
    if data[1] == "get_all_pros":
        # 获取缓存
       
        products = get_all_pros()
        
        clientSocket.send(pickle.dumps((products)))
        return
    if data[1] == "select_product":
        # 查询商品
       
        result, product = select_product(data[2].pro_id)
        
        clientSocket.send(pickle.dumps((result, product)))
        return
    if data[1] == "update_product":
        # 更新商品
       
        result = update_product(data[2])
        
        clientSocket.send(pickle.dumps((result)))
        return
    if data[1] == "add_product":
        # 添加商品
       
        result = add_product(data[2])
        
        clientSocket.send(pickle.dumps((result)))
        return
    if data[1] == "select_new_pro":
        # 查询最新添加的数据
       
        product = select_new_pro()
        
        clientSocket.send(pickle.dumps((product)))
        return
