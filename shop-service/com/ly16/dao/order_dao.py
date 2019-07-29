from com.ly16.domain.Order import Order
from com.ly16.util.db_util import get_mysql_conn


def select_all_order():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()
    # 3.构造SQL语句
    sql = "select order_id,user_id,pro_id,buy_num,address,order_stat,order_time from orders"
    rows = cur.execute(sql)
    if rows > 0:

        orders = cur.fetchall()
        list1 = []
        for order in orders:
            order = Order(order[0], order[1], order[2], order[3], order[4], order[5], order[6])
            list1.append(order)
        
        return list1
        # print(pros)
    else:
        print("未查询到订单！")
        return None


def insert_order(order):
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "insert into orders(user_id, pro_id, buy_num,address) value(%d,%d,%d,'%s')" % (
        order.user_id, order.pro_id, order.buy_num, order.address)
    order.show_order()

    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # 5.处理结果
        if rows > 0:
            # print("商品插入成功！")
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
    return True


def select_desc():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT order_id FROM orders ORDER BY order_id DESC LIMIT 1"
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # print(rows)

        # 5.处理结果
        if rows > 0:
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
            return cur.fetchone()[0]  # 返回的是一个ID
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
        print("商品查询失败！")
    finally:
        cur.close()
        conn.close()


def select_ord(order_id):
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT order_id,user_id, pro_id, buy_num,address,order_stat,order_time FROM orders WHERE order_id=%d" % (order_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # print(rows)

        # 5.处理结果
        if rows > 0:
            # print("商品查询成功！")
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
            order = cur.fetchone()
            order = Order(order[0], order[1], order[2], order[3], order[4], order[5], order[6])
            return True, order
        else:
            return False, None
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
        print("商品查询失败！")
    finally:
        cur.close()
        conn.close()


def delete_order(order_id):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "delete from orders where order_id=%d" % (order_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            pass
            # print("商品删除成功！")
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        else:
            return False
        conn.commit()
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源

    finally:
        cur.close()
        conn.close()
    return True


def update_order(order):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "update orders set user_id=%d,pro_id=%d,buy_num=%d,address='%s',order_stat='%s' where order_id=%d" % (
        order.user_id, order.pro_id, order.buy_num, order.address, order.order_stat, order.order_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            pass
            # print("订单更新成功！")
        # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        else:
            return False
        conn.commit()
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
    finally:
        cur.close()
        conn.close()
    return True


def update_order_stat(order_id, order_new_stat):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "update orders set order_stat='%s' where order_id=%d" % (order_new_stat, order_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            pass
            # print("订单更新成功！")
        # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
        else:
            return False
        conn.commit()
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
    finally:
        cur.close()
        conn.close()
    return True
