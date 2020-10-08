from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=40, primary_key=True, default='')
    user_password = models.CharField(max_length=100, null=True)
    user_email = models.CharField(max_length=50)


class Type_id(models.Model):
    class_id = models.IntegerField()
    class_name = models.CharField(max_length=50)
    father_id = models.IntegerField()


class Goods(models.Model):
    goods_id = models.IntegerField(primary_key=True)  # 商品编号
    goods_name = models.CharField(max_length=50)  # 商品名称
    picture = models.CharField(max_length=100)  # 图片
    class_id = models.ForeignKey(Type_id, on_delete=models.CASCADE, default='')  # 类型ID
    price = models.FloatField()  # 原价
    secprice = models.FloatField()  # 二手价格
    condition = models.CharField(max_length=50)  # 新旧程度
    user_name = models.CharField(max_length=20)  # 卖家名称
    goods_num = models.IntegerField()  # 商品数量


class Messages(models.Model):
    mes_id = models.IntegerField(primary_key=True)  # 留言编号
    mes_type = models.IntegerField(default=1)  # 一级留言,二级回复,1~商品留言,2~对留言的回复信息
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default='default')  # 留言所属用户名
    mes_content = models.CharField(max_length=200)  # 留言内容
    res_id = models.IntegerField(null=True)  # 留言回复id对应mes_id
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, default='')
    mes_time = models.DateTimeField()


class Order(models.Model):
    order_id = models.IntegerField()
    buyer_name = models.CharField(max_length=20)  # 买家名称
    seller_name = models.CharField(max_length=20)  # 卖家名称
    rec_name = models.CharField(max_length=20)  # 收货人姓名
    address = models.CharField(max_length=50)  # 收货人地址
    tel = models.IntegerField()  # 收货人电话
    email = models.CharField(max_length=20)  # 收货人邮箱
    order_time = models.DateTimeField()  # 订单时间
    cost = models.FloatField()  # 订单总价
    state = models.CharField(max_length=20)  # 订单状态
    send = models.CharField(max_length=20)  # 订单配送方式


class Orderdetail(models.Model):
    detail_id = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default='')
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, default='', null=True)
    goods_name = models.CharField(max_length=20)
    goods_price = models.FloatField()
    goods_num = models.IntegerField()
    goods_cost = models.FloatField()


class favorites(models.Model):
    goods_id = models.ForeignKey(Goods, on_delete=models.SET_NULL, default='', null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
