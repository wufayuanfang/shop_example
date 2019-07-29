

'''
Created on 2019年7月25日

@author: 卢艺
'''
from com.ly16.dao.user_dao import insert_user, update_use, remove_use, select_use, select_use_all, select_desc_user


def validate_admin_user(user_id, password):  # 验证用户
    is_validate, user = select_user(user_id)  # 返回结果和一个对象
    
    if is_validate and password != user.password:  # 密码不同时改变结果
        is_validate = False
        
    return is_validate, user


def add_user(user):  # 添加用户
    return insert_user(user)  # 返回结果（bool）


def remove_user(user_id):  # 删除用户
    return remove_use(user_id)


def update_user(user):  # 修改用户信息
    return update_use(user)


def select_user(user_id):
    return select_use(user_id)  # 返回一个(True/False,user/None)


def get_all_user():
    return select_use_all()


def select_new_user():
    user_id = select_desc_user()

    user_new = select_use(user_id)  # 查找用户返回的是一个(BOOL值,user/None)

    return user_new[1]
