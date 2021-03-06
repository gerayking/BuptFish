from django.db.models import Q

from apps.user.models import Shopcart, Goods


class ShopCartService:
    def getCartByName(self,userName :str):
        """ 获取用户的购物车中的物品
            userId : 用户的id
            userName : 用户名
            只要输入一个就可以查询
        """
        goodsIdList = Shopcart.objects.filter(user_name=userName)
        goodsIdList = [item.goods_id for item in goodsIdList]
        goods = Goods.objects.filter(goods_id__in=goodsIdList)
        return goods

    def addInCart(self, userId: int, goodsId: int):
        """
        加入购物车
        userId : 用户的Id
        goodsId : 商品的Id
        """
        shopcart = Shopcart()
        shopcart.user_id = userId
        shopcart.goods_id = goodsId
        shopcart.save()

    def deleteCart(self, userId: int, goodsId: int):
        """
        从购物车删除
        userId : 用户Id
        goodsId : 商品Id
        """
        goods = Shopcart.objects.get(Q(user_id=userId) & Q(goods_id=goodsId))
        if goods != None:
            goods.delete()
            return True
        return False
shopcartservice = ShopCartService()