
'''
Created on 2019年7月25日

@author: 卢艺
'''
import pickle


def process_common_requst(clientSocket,data):
    clientSocket.send(pickle.dumps("不要回答！不要回答！不要回答！"))
