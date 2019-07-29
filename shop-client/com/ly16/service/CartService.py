import json

from com.ly16.domain.Product import Product

carts = {}  #

# 从Carts.txt中拿出数据


# 增加购物车判断
def add_shop_cart(sign, paly_pro_id, pro_name, pro_price, buy_num):
    list_new = [paly_pro_id, pro_name, pro_price, buy_num]  # 这是一个购物车的其中一条信息，以列表方式保存
    lists = []
    
    # 从Carts.json文件中拿出数据
    fp = open('Carts.json', 'r+')
    data = fp.read()
    carts = json.loads(data)
    fp.close()
    
    sign = str(sign)
    plays = carts.get(sign, False)  # 拿到购物车的数据，拿不到则返回False
    if plays == False:  # 当购物车为空时执行操作
        lists.append(list_new)  # 以列表的形式添加到一个大的列表中
        # print(lists)
        carts[sign] = lists  # 把大列表加到字典中

    else:  # 当购物车里面已经存在数据
        # print(carts[sign])
        for play in plays:
            if play[0] == paly_pro_id:  # 在购车找是否存在同一个商品
                play[3] = play[3] + buy_num  # 增加这个商品的数量，不增加新的条目
                break
        else:  # 购物车没有同一个商品
            plays.append(list_new)  # 给购物车添加一条新条目
            carts[sign] = plays  # 覆盖掉原来的购物车

        # print(carts[sign])
        
    # 把数据添加到Carts.txt中
    fp = open('Carts.json', 'w+')
    data = json.dumps(carts, ensure_ascii=False)
    fp.write(data)
    fp.close()

    return True

# else:
#     carts[sign] = [paly_pro_id, pro_name, pro_price, buy_num]


def add_pro_to_cart(pros, paly_pro_id, buy_num, sign):  # 添加商品到购物车
    for pro in pros:
        if paly_pro_id == pro.pro_id:  # 在缓存中找到这个商品信息
            pro_name = pro.pro_name  # 拿到缓存中的数据
            pro_price = pro.pro_price
            pro_num = pro.pro_num
            break
    else:
        return "nnfine"  # 找不到添加的商品，返回提示
    if buy_num > pro_num:
        return "bignum"  # 添加的商品数量超出在售商品数量，返回提示

    add_ord = add_shop_cart(sign[0], paly_pro_id, pro_name, pro_price, buy_num)  # 把数据提交到购物车
    # print(sign[0])
    if add_ord:  # 根据添加操作返回的成否信息判断是否修改缓存中的数据
        # 修改缓存的数量
        for pro in pros:
            if paly_pro_id == pro.pro_id:
                pro.pro_num = pro.pro_num - buy_num
                if pro.pro_num == 0:  # 如果缓存中的商品卖空了，删除没有数量的缓存
                    pros.remove(pro)
        return True
    else:
        return False


# 统计购物车的总价
def show_pro_to_cart(sign):
    carts = show_all_order(sign[0])
    if not carts:
        return False, None
    else:
        sum = 0
        for cart in carts:
            sum = sum + cart[2] * cart[3]
        return carts, sum


# 修改购物车中的商品
def change_cart_num(sign, pro_id, new_buy_num, pros):
    # 从Carts.json文件中拿出数据
    fp = open('Carts.json', 'r+')
    data = fp.read()  # 拿到的数据时字符串
    carts = json.loads(data)  # 转化为原来的样子（字典）
    fp.close()  # 关闭文件连接
    
    sign = str(sign[0])  # 转化后的键变成了字符串，所以先把ID变成字符串才能查询
    lists = carts.get(sign, False)  # 跟据接收的用户ID返回该用户的购物车数据，如果没有数据则返回False
    # 拿到原来的购物车
    if not lists:
        return "none_cart"
    else:
        if new_buy_num == 0:
            del_cart([sign, 1], pros, pro_id)
            return
        for cart in lists:
            if cart[0] == pro_id:  # 在购物车找到这个商品
                if cart[3] <= new_buy_num:
                    change_num = new_buy_num - cart[3]
                    # change_opder(sign, carts)  # 调用修改函数，传递一个新的购物车
                    for pro in pros:  # 更改缓存缓存
                        if pro_id == pro.pro_id:
                            pro.pro_num = pro.pro_num - change_num  # 修改缓存商品数量
                            if pro.pro_num < 0:
                                pro.pro_num = pro.pro_num + change_num  # 恢复修改的缓存商品数量
                                return "bignum"
                            if pro.pro_num == 0:
                                pros.remove(pro)
                    cart[3] = new_buy_num  # 更改购物车
                else:
                    change_num = cart[3] - new_buy_num
                    cart[3] = new_buy_num
                    # change_opder(sign, carts)  # 调用修改函数，传递一个新的购物车
                    for pro in pros:  # 同步缓存
                        if pro_id == pro.pro_id:
                            pro.pro_num = pro.pro_num + change_num
            
            print(lists)
            carts[sign] = lists  # 给ID换新的Value（购物车）
              
            fp = open('Carts.json', 'w+')  # 把新购物车存到Carts.json中
            data = json.dumps(carts, ensure_ascii=False)
            fp.write(data)
            fp.close()
            break
        else:
            return "nofine"  # 找不到商品返回提示


# 删除购物车的商品
def del_cart(sign, pros, pro_id_del):
    # 从Carts.json文件中拿出数据
    fp = open('Carts.json', 'r+')
    data = fp.read()  # 拿到的数据时字符串
    carts = json.loads(data)  # 转化为原来的样子（字典）
    fp.close()  # 关闭文件连接
    
    sign = str(sign[0])  # 转化后的键变成了字符串，所以先把ID变成字符串才能查询
    lists = carts.get(sign, False)  # 跟据接收的用户ID返回该用户的购物车数据，如果没有数据则返回False
    # 拿到原来的购物车
    if not lists:
        return "none_cart"  # 找不到购物车返回提示
    else:
        for cart in lists:
            if cart[0] == pro_id_del:  # 在购物车找到这个商品
                for pro in pros:  # 修改缓存
                    if pro.pro_id == pro_id_del:
                        pro.pro_num = pro.pro_num + cart[3]
                        break
                else:
                    pros.append(Product(cart[0], cart[1], cart[2], cart[3]))
                lists.remove(cart)  # 删除购物车
                
                carts[sign] = lists  # 给ID换新的Value（购物车）  
                
                fp = open('Carts.json', 'w+')  # 把新购物车存到Carts.json中
                data = json.dumps(carts, ensure_ascii=False)
                fp.write(data)
                fp.close()
                return True
        else:
            return "nofine"  # 找不到商品返回提示

        
# 显示购物车
def show_all_order(sign):
    # 从Carts.json文件中拿出数据
    fp = open('Carts.json', 'r+')
    data = fp.read()  # 拿到的数据时字符串
    carts = json.loads(data)  # 转化为原来的样子（字典）
    fp.close()  # 关闭文件连接
    
    sign = str(sign)  # 转化后的键变成了字符串，所以先把ID变成字符串才能查询
    lists = carts.get(sign, False)  # 跟据接收的用户ID返回该用户的购物车数据，如果没有数据则返回False
    return lists

# def change_opder(sign, new_carts):
#     print(new_carts)
