import traceback

from com.ly16.domain.User import User
from com.ly16.main import show_Main_View
from com.ly16.service.user_service import select_new_user, add_user, \
    net_validate_admin_user


def login(pros, users, orders):
    print("####################神州通联在线商城######################")
    print("1.登录 2.注册 3.退出系统")
    op = input()
    if op == "1":

        try:
            user_id = int(input("请输入你的用户ID:"))
            password = input("请输入你的密码：")
        except ValueError:  # 明确捕获ValueError
            print("ID输入有误，应输入数字！")
            login(pros, users, orders)
        except:
            print("发现未知异常")
            print(traceback.format_exc())
            # 网络验证后台管理员

        user = User(user_id, "这是一个假的值", password, "None", "None")

        is_validate_success, is_admin = net_validate_admin_user(user)

        if is_validate_success:
            print("登录成功！！")
            
            show_Main_View(pros, users, orders, [user_id, is_admin])  # 返回ID和权限
        else:
            print("ID或密码输入错误！请重试！")
            login(pros, users, orders)

    elif op == "2":
        user_name = input("请输入添加用户的用户名：")
        user_password = input("请输入添加用户的用户密码：")
        user_address = input("请输入添加用户的用户地址：")
        user = User(1, user_name, user_password, user_address, 'N')
        uadd = add_user(user)
        if not uadd:
            print("用户注册失败！")
            login(pros, users, orders)
        else:
            print("用户注册成功")
            # 向数据库查询该表的最后一条数据的编号，也就是我们刚刚添加的数据
            user_new = select_new_user()
            users.append(user_new)  # 向缓存中添加刚注册的信息
            login(pros, users, orders)

    elif op == "3":
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    else:
        print("输入错误！！！")
        login(pros, users, orders)
