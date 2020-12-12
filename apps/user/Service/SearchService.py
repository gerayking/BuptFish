
from apps.user.models import Goods, Type_id,UserInfo

class SearchService:
    def getGoodsByname(self, name ):
        goods= Goods.objects.filter(state="not_in_order")
        return goods.filter(goods_name=name)
    def getUsersByname(self,name):
        return UserInfo.objects.filter(username=name)