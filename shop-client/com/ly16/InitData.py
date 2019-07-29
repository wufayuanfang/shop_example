from com.ly16.login import login
from com.ly16.service.order_service import get_all_order
from com.ly16.service.product_service import get_all_pros

# 变化不大的数据预先加载，缓存
from com.ly16.service.user_service import get_all_user

if __name__ == '__main__':
    pros = get_all_pros()  # 商品缓存
    users = get_all_user()  # 用户缓存
    orders = get_all_order()  # 订单缓存

    login(pros, users, orders)  # 登录注册页面
