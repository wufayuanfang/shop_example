"""
#商城主界面#
by:joel
emil:dfd888@qq.com
"""
# 脚本代码

# 定义函数
from com.ly16.view.BgMainView import show_bg_main_view
from com.ly16.view.FgMainView import show_fgmain_view
import traceback


def show_Main_View(pros, users, orders, sign):
    print("####################XXXX在线商城######################")
    print("选择操作：1.前台购物 2.后台管理 3.退出系统 4.回到登录")
    try:
        operation = int(input())
    except ValueError:  # 明确捕获ValueError
      # print(traceback.format_exc())
        print("输入有误，应输入（0~3）数字！")
        show_Main_View(pros, users, orders, sign)
    except:
        print("发现未知异常")
        print(traceback.format_exc())
    else:  # 未发生异常执行
        # print("else")
        pass
    finally:  # 不管异常是否发生，始终会执行
        # print("finally")
        pass

    # 通过缩进表达关系的 IPO:in->process->out
    if operation == 1:
        print("当前位置：前台购物")
        show_fgmain_view(pros, users, orders, sign)
    elif operation == 2:
        print("当前位置：后台管理")
        if sign[1] == "N":
            print("您不是管理员，没有权限进入!")
            show_Main_View(pros, users, orders, sign)
        elif sign[1] == "Y":
            show_bg_main_view(pros, users, orders, sign)
        else:
            print("你的权限参数错误！！！")
            show_Main_View(pros, users, orders, sign)
    elif operation == 3:
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif operation == 4:
        from com.ly16.login import login
        login(pros, users, orders)
    else:
        print("输入错误,应输入（0~3）数字！")

    show_Main_View(pros, users, orders, sign)  # 函数递归调用

# 条件满足表示运行的就是当前模块 ，条件不满足表示被其他模块导入使用
# if __name__ == '__main__':
#     show_Main_View()
