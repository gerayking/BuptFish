import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from BuptFish import settings


def user_director_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(instance.username, ext)
    return os.path.join(instance.username, filename)


class UserInfo(AbstractUser):
    avatar = models.ImageField('头像', upload_to=user_director_path,
                               default="https://i.loli.net/2020/11/08/KnofmQWD15BxcMu.jpg")

class ShopCart(models.Model):
    user_name = models.CharField(null=False,max_length=150)
    goods_id = models.IntegerField(null=False)

class Type_id(models.Model):
    class_id = models.IntegerField(default=0)
    class_name = models.CharField(max_length=50)
    father_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'Type_id'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50)  # 商品名称
    picture = models.CharField(max_length=100)  # 图片
    class_id = models.IntegerField(default=0)  # 类型的ID
    description = models.CharField(max_length=200)
    # Class = models.ForeignKey(Type_id, on_delete=models.CASCADE, default='')  # 类型ID
    price = models.FloatField()  # 原价
    secprice = models.FloatField()  # 二手价格
    condition = models.CharField(max_length=50)  # 新旧程度
    user_name = models.CharField(max_length=20)  # 卖家名称
    goods_num = models.IntegerField()  # 商品数量

    class Meta:
        db_table = 'Goods'


class Messages(models.Model):
    mes_id = models.IntegerField(primary_key=True)  # 留言编号
    mes_type = models.IntegerField(default=1)  # 一级留言,二级回复,1~商品留言,2~对留言的回复信息
    user_name = models.CharField(max_length=50)  # 留言所属用户名
    mes_content = models.CharField(max_length=200)  # 留言内容
    res_id = models.IntegerField(null=True)  # 留言回复id对应mes_id
    goods_id = models.IntegerField(default=0)
    # goods = models.ForeignKey(Goods, on_delete=models.CASCADE, default='')
    mes_time = models.DateTimeField()

    class Meta:
        db_table = 'Messages'


class Order(models.Model):
    order_id = models.IntegerField()
    buyer_id = models.IntegerField()# 买家名称
    seller_id= models.IntegerField() # 卖家名称
    rec_name = models.CharField(max_length=20)  # 收货人姓名
    address = models.CharField(max_length=50)  # 收货人地址
    tel = models.IntegerField()  # 收货人电话
    email = models.CharField(max_length=20)  # 收货人邮箱
    order_time = models.DateTimeField()  # 订单时间
    cost = models.FloatField()  # 订单总价
    state = models.CharField(max_length=20)  # 订单状态
    send = models.CharField(max_length=20)  # 订单配送方式

    class Meta:
        db_table = 'Order'


class Orderdetail(models.Model):
    detail_id = models.IntegerField()
    order_id = models.IntegerField(default=0)
    goods_id = models.IntegerField(default=0)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')
    # goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, default='', null=True)
    goods_name = models.CharField(max_length=20)
    goods_price = models.FloatField()
    goods_num = models.IntegerField()
    goods_cost = models.FloatField()

    class Meta:
        db_table = 'Orderdetail'


class Collect(models.Model):
    goods_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=150)

    # goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, default='', null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'collect'
