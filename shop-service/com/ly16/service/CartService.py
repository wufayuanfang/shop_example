from com.ly16.domain.Product import Product
from com.ly16.service.shop_cart import add_shop_cart, show_all_order


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
    carts = show_all_order(sign[0])  # 拿到原来的购物车
    if not carts:
        return "none_cart"
    else:
        if new_buy_num == 0:
            del_cart(sign, pros, pro_id)
            return
        for cart in carts:
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

                break
        else:
            return "nofine"  # 找不到商品返回提示


# 删除购物车的商品
def del_cart(sign, pros, pro_id_del):
    carts = show_all_order(sign[0])  # 拿到原来的购物车
    if not carts:
        return "none_cart"  # 找不到购物车返回提示
    else:
        # print(carts)
        for cart in carts:
            if cart[0] == pro_id_del:  # 在购物车找到这个商品
                for pro in pros:  # 修改缓存
                    if pro.pro_id == pro_id_del:
                        pro.pro_num = pro.pro_num + cart[3]
                        break
                else:
                    pros.append(Product(cart[0], cart[1], cart[2], cart[3]))
                carts.remove(cart)
                return True
        else:
            return "nofine"  # 找不到商品返回提示
