from com.ly16.domain.User import User
from com.ly16.util.db_util import get_mysql_conn


# 添加用户
def insert_user(user):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "INSERT INTO users(user_name, PASSWORD, address, is_admin) VALUE('%s','%s','%s','%s')" % (
        user.user_name, user.password, user.address, user.is_admin)

    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            # print("添加用户成功！")
            pass
        else:
            return False
        # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        conn.commit()
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
    finally:
        cur.close()
        conn.close()
    return True  # 返回结果


# 删除用户
def remove_use(user_id):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "delete from users where user_id=%d" % (user_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            print("用户删除成功！")
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        else:
            return False
        conn.commit()
    except:
        return False
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源

    finally:
        cur.close()
        conn.close()
    return True


# 更新用户信息
def update_use(user):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "UPDATE users SET user_name='%s', PASSWORD='%s', address='%s', is_admin='%s' WHERE user_id=%d" % (
        user.user_name, user.password, user.address, user.is_admin, user.user_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            # print("用户更新成功！")
            pass
        # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        else:
            return False  # 返回更新失败结果
        conn.commit()
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
    finally:
        cur.close()
        conn.close()
    return True  # 返回结果


# 查询用户
def select_use(user_id):
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT user_id,user_name,password,address,is_admin FROM users WHERE user_id=%d" % (user_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # print(rows)

        # 5.处理结果
        if rows > 0:
            row = cur.fetchone()
            user = User(row[0], row[1], row[2], row[3], row[4])
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
            return True, user
        else:
            return False, None
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
        print("商品查询失败！")
    finally:
        cur.close()
        conn.close()


def select_use_all():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()
    # 3.构造SQL语句
    sql = "select user_id,user_name,password,address,is_admin from users"
    rows = cur.execute(sql)
    if rows > 0:

        users = cur.fetchall()
        list1 = []
        for user in users:
            user = User(user[0], user[1], user[2], user[3], user[4])
            list1.append(user)

        return list1
    else:
        print("未查询到商品！")

    return None


def select_desc_user():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1"
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # print(rows)

        # 5.处理结果
        if rows > 0:
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
            return cur.fetchone()[0]
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
        print("用户查询失败！")
    finally:
        cur.close()
        conn.close()
