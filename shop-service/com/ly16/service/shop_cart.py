carts = {}  #


# 添加商品到购物车
def add_shop_cart(sign, paly_pro_id, pro_name, pro_price, buy_num):
    list_new = [paly_pro_id, pro_name, pro_price, buy_num]  # 这是一个购物车的其中一条信息，以列表方式保存
    lists = []
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

    return True


# else:
#     carts[sign] = [paly_pro_id, pro_name, pro_price, buy_num]

# 显示购物车
def show_all_order(sign):
    lists = carts.get(sign, False)  # 跟据接收的用户ID返回该用户的购物车数据，如果没有数据则返回False
    return lists

# def change_opder(sign, new_carts):
#     print(new_carts)
# carts[sign] = new_carts

# add_shop_cart(1000, 1024, 'ttttt', 99.9, 45)
# add_shop_cart(1000, 1000, 'fggg', 449, 45)
#
# add_shop_cart(1022, 1000, 'fggg', 449, 45)
# add_shop_cart(1022, 2222, 'oooo', 111, 111)
