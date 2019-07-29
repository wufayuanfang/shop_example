import MySQLdb


def get_mysql_conn():
    conn = MySQLdb.connect(db="sztlshop", host="localhost", port=3306, user="root", passwd="123456", charset="utf8")
    # print(conn)

    return conn


if __name__ == '__main__':
    get_mysql_conn()
