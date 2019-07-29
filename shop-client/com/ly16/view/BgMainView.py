from com.ly16.view.OrderMainView import show_order_main_view
from com.ly16.view.ProMgrView import showProMgrView
from com.ly16.view.UserMgrView import showUserMgrView


def show_bg_main_view(pros, users, orders, sign):
    print("==============后台购物主界面==============")
    print("请选择操作：1.商品管理 2.用户管理 3退出系统 4.返回 5.订单管理")
    bg_oper = input()

    if bg_oper == "1":
        print("商品管理")
        showProMgrView(pros, users, orders, sign)
    elif bg_oper == "2":
        print("用户管理")
        showUserMgrView(pros, users, orders, sign)
    elif bg_oper == "3":
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif bg_oper == "4":
        from com.ly16.main import show_Main_View
        show_Main_View(pros, users, orders, sign)
    elif bg_oper == "5":
        print("订单管理")
        show_order_main_view(pros, users, orders, sign)
    else:
        print("输入有误，请输入（1~5）数字！")

    show_bg_main_view(pros, users, orders, sign)
    # return 结束函数调用
    # return 'result' #返回单个值

    # return True, "result"  # 返回多个值


# 匿名函数：之前是参数，：之后是执行语句，并返回


if __name__ == '__main__':
    # x, y = show_bg_main_view()
    # print(x)
    # print(y)
    pass  # 啥都不做，只是凑成语法正确
