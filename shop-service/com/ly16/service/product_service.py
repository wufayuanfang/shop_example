from com.ly16.dao.product_dao import insert_pro, remove_pro, update_pro, select_pro, select_all_pros, select_desc


def add_product(pro):  # 添加商品
    return insert_pro(pro)  # 返回结果（BOOL）


def remove_product(pro_id):  # 删除一个商品
    return remove_pro(pro_id)


def update_product(pro):
    return update_pro(pro)


def select_product(pro_id):
    return select_pro(pro_id)


def get_all_pros():
    # 1.用户验证()
    # 2.权限认证，鉴权
    # 数据稽核（证据保留），写日志
    return select_all_pros()


def select_new_pro():
    id = select_desc()
    # print(id)
    pro_new = select_pro(id)

    return pro_new[1]
