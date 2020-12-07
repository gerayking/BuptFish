from apps.user.models import Goods, favorites, UserInfo


def collectview(c_id):
    favor = favorites.objects.filter(user=c_id)
    good = Goods.objects.filter(goods_id__in=favor)
    return good
