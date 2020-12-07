
class ShopCartService:
    def getCartById(self, userId : int ,userName :str):
        """ 获取用户的购物车中的物品
            userId : 用户的id
            userName : 用户名
            只要输入一个就可以查询
            """

    def addInCart(self, userId: int, goodsId: int):
        """
        加入购物车
        userId : 用户的Id
        goodsId : 商品的Id
        """

    def deleteCart(self, userId: int, goodsId: int):
        """
        从购物车删除
        userId : 用户Id
        goodsId : 商品Id
        """
