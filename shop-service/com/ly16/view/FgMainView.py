from com.ly16.domain.Order import Order
from com.ly16.domain.Product import Product
from com.ly16.service.CartService import add_pro_to_cart, show_pro_to_cart, change_cart_num, del_cart
from com.ly16.service.order_service import add_order, select_new_order, select_order
from com.ly16.service.product_service import select_product, remove_product, update_product
from com.ly16.service.shop_cart import add_shop_cart, show_all_order
import traceback


def show_fgmain_view(pros, users, orders, sign):
    print("==============前台购物主界面==============")
    print("==============在售商品列表================")
    # 获取所有商品
    for pro in pros:
        pro.show_pro()
    print("==============在售商品列表================")
    print("选择操作：1、购买商品 2、显示购物车、 3、修改购买数量 4、删除购物项 5、结账 6、系统退出 7、返回")
    user_oper = input()
    if user_oper == "1":
        print("购买商品")

        try:
            paly_pro_id = int(input("输入你要购买的商品编号："))  # 先拿到编号然后获取到商品别的数据
            buy_num = int(input("输入你要购买的商品数量："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("输入有误，应输入数字！")
            show_fgmain_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        add_retuen = add_pro_to_cart(pros, paly_pro_id, buy_num, sign)
        if add_retuen == "nnfine":
            print("没有找到这个商品哦！！！")
            show_fgmain_view(pros, users, orders, sign)
        if add_retuen == "bignum":
            print("购买数量太大，商品不足！")
            show_fgmain_view(pros, users, orders, sign)
        if add_retuen:
            print("已添加到购物车！！！")
            show_fgmain_view(pros, users, orders, sign)
        else:
            print("添加购物车失败！！！")
            show_fgmain_view(pros, users, orders, sign)

    elif user_oper == "2":
        print("显示购物车")
        print("=" * 40)
        print("购物车：")
        carts, sum = show_pro_to_cart(sign)
        if carts:
            for cart in carts:
                print("商品ID：%d  商品名称：%s  商品价格：%.2f 商品数量：%d" % (cart[0], cart[1], cart[2], cart[3]))
            print("总价：%.2f" % sum)
        else:
            print("购物车为空！")
        print("=" * 40 + '\n')
    elif user_oper == "3":
        print("修改购买数量")

        try:
            pro_id = int(input("输入要修改的商品编号："))
            new_buy_num = int(input("输入要修改的商品数量："))
        except ValueError:  # 明确捕获ValueError
            print(traceback.format_exc())
            print("输入有误，应输入数字！")
            show_fgmain_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        change_return = change_cart_num(sign, pro_id, new_buy_num, pros)
        if change_return == "none_cart":
            print("购物车为空！！！")
            show_fgmain_view(pros, users, orders, sign)
        if change_return == "bignum":
            print("输入的商品数量超出了在售的商品数量！")
            show_fgmain_view(pros, users, orders, sign)
        if change_return == "nofine":
            print("找不到这个商品！！！")
            show_fgmain_view(pros, users, orders, sign)
    elif user_oper == "4":
        print("删除购物项")

        try:
            pro_id_del = int(input("输入要删除的商品编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("输入有误，应输入数字！")
            show_fgmain_view(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        del_return = del_cart(sign, pros, pro_id_del)
        if del_return == "none_cart":
            print("购物车为空！！！")
            show_fgmain_view(pros, users, orders, sign)
        if del_return == "nofine":
            print("找不到这个商品！！！")
            show_fgmain_view(pros, users, orders, sign)
        if del_return:
            print("删除购物项成功!")

    elif user_oper == "5":

        # 1.支付
        print("结账")
        # 2.生产订单
        carts = show_all_order(sign[0])  # 拿到原来的购物车
        if not carts:
            print("购物车为空！！！")
        else:
            # print(carts)
            for cart in carts:
                print(carts)
                address = input("请输入商品：" + str(cart[0]) + "," + cart[1] + "的收货地址：")
                order_new = Order(1, sign[0], cart[0], cart[3], address, 'A')
                sadd = add_order(order_new)
                if not sadd:
                    print("订单添加失败！")
                else:
                    print("订单" + str(cart[0]) + "添加成功!")
                    # 向数据库查询该表的最后一条数据的编号，也就是我们刚刚添加的数据

                    # 更新数据库的商品信息
                    selt = select_product(cart[0])
                    # if selt[1].pro_num == cart[3]:  # 如果是买完当前商品的全部数量
                    #     remove_product(cart[0])  # 在库存里把余量为0的商品删除  #因为外键存在，所以删除失败
                    # else:
                    selt[1].pro_num = selt[1].pro_num - cart[3]  # 更新库存余量
                    pro = Product(cart[0], cart[1], cart[2], selt[1].pro_num)
                    update_product(pro)

                    order = select_new_order()  # 更新订单缓存
                    order = Order(order[0], order[1], order[2], order[3], order[4], order[5])
                    orders.append(order)
                    # carts.remove(cart)#删除后商品项往前移，指针在后，影响执行
            else:
                carts.clear()  # 结账之后清空购物车

        # 3.持久化生产库存
    elif user_oper == "6":
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif user_oper == "7":
        # 运行时才会导入，延迟导入
        from com.ly16.main import show_Main_View
        show_Main_View(pros, users, orders, sign)
    else:
        print("输入错误！")

    show_fgmain_view(pros, users, orders, sign)


if __name__ == '__main__':
    print("Fg View")
