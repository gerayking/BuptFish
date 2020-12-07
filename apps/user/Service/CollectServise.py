from apps.user.models import Goods,favorites,UserInfo

def collectview(c_id):
    favor=favorites.objects.get(id=c_id)
    good=Goods.objects.filter(goods_id=favor.goods_id)
    return good