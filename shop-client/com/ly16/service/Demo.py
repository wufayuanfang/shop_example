'''
Created on 2019年7月26日

@author: 卢艺
'''
import json
import sys


carts = {1000: [[1027, '辽宁舰', 2000000000.0, 1], [1024, '作业本', 1.5, 5000], [1017, '步步高点读机', 2222.0, 20000]], 1003: [[1018, '诺基亚C', 1999.0, 5000], [1024, '作业本', 1.5, 5000], [1023, '新华字典', 49.9, 1000]], 1004: [[1024, '作业本', 1.5, 2222], [1018, '诺基亚C', 1999.0, 421]]}

if __name__ == '__main__':
#     fp = open('Carts.json', 'w+')
#     data = json.dumps(carts,ensure_ascii=False)
#     fp.write(data)
#     fp.close()

#     fp = open('Carts.json', 'r+')
#     data = fp.read()
# #     data = json.loads(data)
#     print(data)

    sys.stderr.write('Warning, log file not found starting a new one\n')