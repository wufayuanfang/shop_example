import traceback

from com.ly16.domain.Order import Order
from com.ly16.domain.Product import Product
from com.ly16.service.order_service import add_order, select_new_order, select_order, remove_order, change_order, \
    modify_order_stat
from com.ly16.service.product_service import select_product, update_product
from com.ly16.service.user_service import select_user


def show_order_main_view(pros, users, orders, sign):
    print("==============订单主界面==============")
    print("=====================订单列表=================")
    # 获取牌所有订单
    for order_lists in orders:
        order_lists.show_order()
    print("=====================订单列表=================")
    print("请选择操作：1.VIP下单 2.删除订单 3.修改订单 4订单详情5.退出系统 6.返回")
    order_oper = input()
    if order_oper == "1":
        print("VIP下单")

        try:
            user_id = int(input("请输入用户编号："))
            pro_id = int(input("请输入商品编号："))
            buy_num = int(input("请输入购买数量："))
            address = input("请输入收货地址：")
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("输入有误，应输入数字！")
            show_order_main_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        selt = select_product(pro_id)  # 在数据库去寻找这个商品
        if selt[1].pro_num < buy_num:
            print("购买商品数量过大，剩余库存:%d" % selt[1].pro_num)
            show_order_main_view(pros, users, orders, sign)
        if not selt[0]:
            print("不存在这个商品编号！")
            show_order_main_view(pros, users, orders, sign)
        uselt = select_user(user_id)
        if not uselt[0]:
            print("不存在这个用户编号！！！")
            show_order_main_view(pros, users, orders, sign)
        order_new = Order(1, user_id, pro_id, buy_num, address, 'A')
        sadd = add_order(order_new)
        if not sadd:
            print("订单添加失败！")
        else:
            print("订单添加成功")
            # 向数据库查询该表的最后一条数据的编号，也就是我们刚刚添加的数据
            order = select_new_order()
            order = Order(order[0], order[1], order[2], order[3], order[4], order[5])
            orders.append(order)  # 更新订单缓存

            # 更新数据库的商品信息
            selt[1].pro_num = selt[1].pro_num - buy_num  # 更新库存余量
            pro = Product(selt[1].pro_id, selt[1].pro_name, selt[1].pro_price, selt[1].pro_num)
            update_product(pro)
            # 更新商品缓存
            for pro in pros:  # 更新缓存中的商品数量
                if pro.pro_id == pro_id:
                    pro.pro_num -= buy_num
    elif order_oper == "2":
        print("删除订单")

        try:
            order_id = int(input("请输入要删除的订单编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("订单编号输入有误，应输入数字！")
            show_order_main_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())
        selt = select_order(order_id)  # 查询这个订单数据
        print(selt[1])

        if not selt[0]:
            print("找不到这个订单！！！")
            show_order_main_view(pros, users, orders, sign)
        sdel = remove_order(order_id)  # 删除订单
        if not sdel:
            print("删除订单失败！")
            show_order_main_view(pros, users, orders, sign)
        else:
            print("删除订单成功！")
            for order in orders:  # 更新缓存
                if order.order_id == order_id:
                    orders.remove(order)

            # 删除订单时订单的商品应恢复到数据库和缓存
            prot = select_product(selt[1][2])  # 向数据库找到这个商品
            prot[1].pro_num += selt[1][3]  # 更新库存余量
            pro = Product(prot[1].pro_id, prot[1].pro_name, prot[1].pro_price, prot[1].pro_num)
            update_product(pro)  # 向数据库提交更新数据

            # 释放商品到缓存
            for pro in pros:
                if pro.pro_id == selt[1][2]:
                    pro.pro_num += selt[1][3]


    elif order_oper == "3":
        print("修改订单")

        try:
            order_id = int(input("请输入要修改的订单编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("订单编号输入有误，应输入数字！")
            show_order_main_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())
        selt = select_order(order_id)
        if not selt[0]:
            print("没有这个订单编号！")
            show_order_main_view(pros, users, orders, sign)
        stat = input("请输入订单状态（A：新订单 B:配货中 C：物流中 D:已签收 E:可归档）")

        # user_id = int(input("请输入新的用户编号："))
        # pro_id = int(input("请输入新的商品编号："))
        # buy_num = int(input("请输入新的购买数量："))
        # address = input("请输入新的收货地址：")
        # stat = input("请输入订单状态：")
        # selt = select_product(pro_id)
        # if not selt[0]:
        #     print("不存在这个商品编号！")
        #     show_order_main_view(pros, users, orders, sign)
        # uselt = select_user(user_id)
        # if not uselt[0]:
        #     print("不存在这个用户编号！！！")
        #     show_order_main_view(pros, users, orders, sign)
        # order_new = Order(order_id, user_id, pro_id, buy_num, address, stat)
        # colt = change_order(order_new)
        colt = modify_order_stat(order_id, stat)
        if colt:
            print("订单修改成功！！")
            for order in orders:
                if order.order_id == order_id:
                    # order.user_id = user_id
                    # order.pro_id = pro_id
                    # order.buy_num = buy_num
                    # order.address = address
                    order.order_stat = stat
                    # print(order)
        else:
            print("订单修改失败！!")
    elif order_oper == "4":
        print("订单详情")

        try:
            order_id = int(input("请输入要查询的订单编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("订单编号输入有误，应输入数字！")
            show_order_main_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        selt = select_order(order_id)
        if selt[0]:
            lists = list(selt[1])
            print("订单编号：%d" % lists[0])
            print("用户编号：%d" % lists[1])
            print("商品编号：%d" % lists[2])
            print("购买数量：%d" % lists[3])
            print("收货地址：%s" % lists[4])
            print("订单状态：%s" % lists[5])
        else:
            print("查询失败！")
    elif order_oper == "5":
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif order_oper == "6":
        from com.ly16.view.BgMainView import show_bg_main_view
        show_bg_main_view(pros, users, orders, sign)
    else:
        print("输入有误，请输入（1~5）数字！")

    show_order_main_view(pros, users, orders, sign)
    # return 结束函数调用
    # return 'result' #返回单个值

    # return True, "result"  # 返回多个值

    # 匿名函数：之前是参数，：之后是执行语句，并返回

    if __name__ == '__main__':
        # x, y = show_bg_main_view()
        # print(x)
        # print(y)
        pass  # 啥都不做，只是凑成语法正确
