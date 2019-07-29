from com.ly16.domain.Product import Product
from com.ly16.util.db_util import get_mysql_conn


# 添加商品
def insert_pro(pro):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "insert into products(pro_name, pro_price, pro_num) value('%s',%.2f,%d)" % (
        pro.pro_name, pro.pro_price, pro.pro_num)

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


# 删除商品
def remove_pro(pro_id):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "delete from products where pro_id=%d" % (pro_id)
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
        return "nodel"

    finally:
        cur.close()
        conn.close()
    return True


# 更新商品
def update_pro(pro):
    # 1.获取数据库连接
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "update products set pro_name='%s',pro_price=%f,pro_num=%d where pro_id=%d" % (
        pro.pro_name, pro.pro_price, pro.pro_num, pro.pro_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        print(rows)
        # 5.处理结果
        if rows > 0:
            print("商品更新成功！")
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


# 查询商品
# 集合：多值容器
# numpy:多维数组 列表：[]  元祖：(,)  字典{k1:v1,k2:v2} set:无序列表


pros = ()


def select_all_pros():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()
    # 3.构造SQL语句
    sql = "select pro_id,pro_name,pro_price,pro_num from products"
    rows = cur.execute(sql)
    if rows > 0:
        pro_lists = []
        pros = cur.fetchall()
        for pro in pros:
            pro = Product(pro[0], pro[1], pro[2], pro[3])
            pro_lists.append(pro)
        return pro_lists

        # print(pros)
    else:
        print("未查询到商品！")
        return None


if __name__ == '__main__':
    select_all_pros()


def select_pro(pro_id):
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT pro_id,pro_name,pro_price,pro_num FROM products WHERE pro_id=%d" % (pro_id)
    try:

        # 4.执行SQL语句
        rows = cur.execute(sql)
        # print(rows)

        # 5.处理结果
        if rows > 0:
            # print("商品查询成功！")
            # 6.提交事务(insert、delete、updata需要提交事务，select不需要)
            row = cur.fetchone()
            pro = Product(row[0], row[1], row[2], row[3])
            return True, pro
        else:
            return False, None
    except:
        conn.rollback()  # 有异常应该回滚事务
        # 7.关闭连接等资源
        print("商品查询失败！")
    finally:
        cur.close()
        conn.close()


def select_desc():
    conn = get_mysql_conn()

    # 2.获取游标（对象：存储了关联SQL语句影响的数据以及操作数据的功能）

    cur = conn.cursor()

    # 3.构造SQL语句
    sql = "SELECT pro_id FROM products ORDER BY pro_id DESC LIMIT 1"
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
        print("商品查询失败！")
    finally:
        cur.close()
        conn.close()
