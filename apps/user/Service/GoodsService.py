import json

from django.http import HttpResponse, HttpRequest
from django.test import TestCase

from apps.user.models import Goods, Type_id
from apps.user.utils.ClassTree import ClassTree


class GoodService:
    def get_recommend(self):
        return Goods.objects.filter(state=1);
    def getGoodsById(self,gid:int):
        return Goods.objects.get(goods_id=gid)
    def addComment(self,userId:int,content:str,goodsId:int):
        """
        添加商品评论
        userId: 用户的ID
        content: 评论的内容
        goodsId : 商品的Id
        """

    def get_goods_type(self):
        classidlist = Type_id.objects.values("class_name").distinct()
        typenamelist = [item["class_name"] for item in classidlist]
        return typenamelist

    def get_price_dis(self):
        price_list = ["<100", "101-200", "201-500", ">501"]
        return price_list

    def buyGoods(self,userId:int, goodsId:int):
        """
        用户购买物品
        userId : 用户id
        goodsId : 物品名称
        """

    def searchgoods(self, type: str, minprice: int, maxprice: int):
        goodslistall = ClassTree.search(type)
        goodslist = [item for item in goodslistall if minprice <= item.price <= maxprice]
        return goodslist
    # 检查商品的属性是否符合条件,然后再插入数据库
    def releaseGoods(self,goods : Goods):
        status = 200
        msg = list()
        if goods.user_name == "" or goods .user_name == None:
            msg.append("用户名未登录")
            status = 403
        if goods.goods_num == 0 or goods.goods_num == None :
            msg.append("数量不能为零")
            status = 403
        if goods.picture == None or goods.picture == "":
            msg.append("暂无图片")
            goods.picture = "https://i.loli.net/2020/12/06/ZLnWuOce9Isg1wy.jpg"
        if goods.price < 0:
            msg.append("价格不能为负数")
            status = 403
        if goods.goods_name == "" or goods.goods_name == None:
            msg.append("商品名称不能为空")
            status = 403
        if status == 200:
            msg.append("发布成功")
            goods.save()
        return HttpResponse(json.dumps({
            "status" : status,
            "msg" : msg
        }))

goodservice = GoodService()