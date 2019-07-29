import traceback

from com.ly16.domain.User import User
from com.ly16.service.user_service import add_user, update_user, remove_user, select_user, select_new_user


def showUserMgrView(pros, users, orders, sign):
    print("=====================用户管理界面=============")
    print("=====================用户列表=================")
    # 获取牌所有商品
    if users != None:
        for user_lists in users:
            user_lists.show_user()
    print("=====================用户列表=================")
    print("选择操作：1.添加用户 2.修改用户信息 3.删除用户 4.显示用户信息 5.退出系统 6.返回 ")

    user_oper = int(input())

    if user_oper == 1:
        print("添加用户")
        user_name = input("请输入添加用户的用户名：")
        user_password = input("请输入添加用户的用户密码：")
        user_address = input("请输入添加用户的用户地址：")
        user_isadmin = input("是否为管理员（Y/N）：")
        
        user_new = User(1, user_name, user_password, user_address, user_isadmin)  # 生成一个用户对象
        
        uadd = add_user(user_new)
        
        if not uadd:
            print("用户添加失败！")
        else:
            print("用户添加成功")
            # 向数据库查询该表的最后一条数据的编号，也就是我们刚刚添加的数据
            user = select_new_user()
            users.append(user)
    elif user_oper == 2:
        print("修改用户信息")

        try:
            user_id = int(input("请输入修改用户的用户编号："))
            user_name = input("请输入修改用户的用户名：")
            user_password = input("请输入修改用户的用户密码：")
            user_address = input("请输入修改用户的用户地址：")
            user_isadmin = input("是否为管理员（Y/N）：")
            
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("用户编号输入有误，应输入数字！")
            showUserMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        user = User(user_id, user_name, user_password, user_address, user_isadmin)  # 用新的数据生成一个对象
        result = update_user(user)  # 更新用户
        
        if not result:
            print("修改用户信息失败！")
            showUserMgrView(pros, users, orders, sign)
        else:
            print("修改用户信息成功！")
            for use_up in users:  # 更新缓存
                if use_up.user_id == user_id:
                    use_up.user_name = user_name
                    use_up.password = user_password
                    use_up.address = user_address
                    use_up.is_admin = user_isadmin
    elif user_oper == 3:
        print("删除用户")

        try:
            user_id = int(input("请输入删除用户的用户编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("用户编号输入有误，应输入数字！")
            showUserMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        sdel = remove_user(user_id)  # 删除用户
        if not sdel:
            print("不能删除此用户，有订单待此用户接收！")
            showUserMgrView(pros, users, orders, sign)
        else:
            print("删除用户成功！")
            for user in users:
                if user.user_id == user_id:
                    users.remove(user)
    elif user_oper == 4:
        print("显示用户信息")

        try:
            user_id = int(input("请输入查询用户的用户编号："))
        except ValueError:  # 明确捕获ValueError
            # print(traceback.format_exc())
            print("用户编号输入有误，应输入数字！")
            showUserMgrView(pros, users, orders, sign)
        except:
            print("发现未知异常")
            print(traceback.format_exc())

        selt = select_user(user_id)  # 查询用户
        print(5555555)
        if selt[0]:
            selt[1].show_user()
        else:
            print("查询失败！没有这个用户哦！！")
    elif user_oper == 5:
        print("=" * 10 + "您已经退出系统" + "=" * 15)
        exit(0)
    elif user_oper == 6:
        from com.ly16.view.BgMainView import show_bg_main_view
        show_bg_main_view(pros, users, orders, sign)
    else:
        print("输入有误，请输入（1~5）数字！")

    showUserMgrView(pros, users, orders, sign)
