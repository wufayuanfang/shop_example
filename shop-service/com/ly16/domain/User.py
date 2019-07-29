class User(object):

    def __init__(self, user_id, user_name, password, address, is_admin):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.address = address
        self.is_admin = is_admin

    def show_user(self):
        print("用户编号：" + str(self.user_id), "用户名称：" + self.user_name, "用户密码：" + self.password, "收货地址：" + self.address,
              "用户权限：" + self.is_admin)
