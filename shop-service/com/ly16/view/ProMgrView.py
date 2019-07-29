import traceback

from com.ly16.domain.Product import Product
from com.ly16.service.product_service import add_product, remove_product, update_product, select_product, get_all_pros, \
    select_new_pro


def showProMgrView(pros, users, orders, sign):
    print("=====================商品管理界面=============")
    print("=====================商品列表=================")
    # 获取牌所有商品
    for pro_lists in pros:
        pro_lists.show_pro()
    print("=====================商品列表=================")
    print("选择操作：1.商品上架 2.商品下架 3.修改商品信息  4.商品详情 5.退出系统 6.返回 ")

    pro_oper = input()

    if pro_oper == "1":
        print("商品上架")

        try:
            pro_name = input("请输入商品名称：")
            pro_price = float(input("请输入商品价格："))
            pro_num = int(input("请输入商品数量："))
        except ValueError:  # 明确捕获ValueError
            print("输入有误，应输入数字！")
            showProMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        pro = Product(1, pro_name, pro_price, pro_num)  # 因为ID由数据库生成，所以随便传一个参（不生效）
        sadd = add_product(pro)
        if not sadd:
            print("商品添加失败！")
        else:
            print("商品添加成功")
            # 向数据库查询该表的最后一条数据的编号，也就是我们刚刚添加的数据
            pro = select_new_pro()
            pros.append(pro)
    elif pro_oper == "2":
        print("商品下架")

        try:
            pro_id = int(input("请输入要删除的商品编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("商品编号输入有误，应输入数字！")
            showProMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        sdel = remove_product(pro_id)
        if sdel == "nodel":
            print("要删除的商品在用户订单中，不能删除！")
            showProMgrView(pros, users, orders, sign)
        if not sdel:
            print("删除商品失败！")
            showProMgrView(pros, users, orders, sign)
        else:
            print("删除商品成功！")
            for pro in pros:
                if pro.pro_id == pro_id:
                    pros.remove(pro)

    elif pro_oper == "3":
        print("修改商品")

        try:
            pro_id = int(input("请输入要修改的商品编号："))
            pro_name = input("请输入商品新名称：")
            pro_price = float(input("请输入商品新价格："))
            pro_num = int(input("请输入商品新数量："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("输入有误，应输入数字！")
            showProMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        pro = Product(pro_id, pro_name, pro_price, pro_num)
        stat = update_product(pro)
        if not stat:
            print("要修改的商品不存在！")
            showProMgrView(pros, users, orders, sign)
        else:
            print("修改商品信息成功！")
            for pro_up in pros:
                if pro_up.pro_id == pro_id:
                    pro_up.pro_name = pro_name
                    pro_up.pro_price = pro_price
                    pro_up.pro_num = pro_num

    elif pro_oper == "4":
        print("商品详情")
        pro_oper4(pros, users, orders, sign)
    elif pro_oper == "5":
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif pro_oper == "6":
        from com.ly16.view.BgMainView import show_bg_main_view
        show_bg_main_view(pros, users, orders, sign)
    else:
        print("输入有误，请输入（1~5）数字！")

    showProMgrView(pros, users, orders, sign)


def pro_oper4(pros, users, orders, sign):
    try:
        pro_id = int(input("请输入要查询的商品编号："))
    except ValueError:  # 明确捕获ValueError
        # print(traceback.format_exc())
        print("商品编号输入有误，应输入数字！")
        showProMgrView(pros, users, orders, sign)
    except:
        print("发现未知异常")
        print(traceback.format_exc())

    selt = select_product(pro_id)  # 查询商品返回一个有两值得列表：[[布尔值][对象]]
    if selt[0]:
        selt[1].show_pro()

        # print("商品编号：%d" % lists.pro_id)
        # print("商品名称：%s" % lists.pro_name)
        # print("商品价格：%f" % lists.pro_price)
        # print("商品数量：%d" % lists.pro_num)
        print("1.继续查询 2.返回")
        op = input()
        if op == '1':
            pro_oper4(pros, users, orders, sign)
        elif op == '2':
            showProMgrView(pros, users, orders, sign)
        else:
            print("输入错误！返回商品管理界面！")
            showProMgrView(pros, users, orders, sign)
    else:
        print("查询失败！")
