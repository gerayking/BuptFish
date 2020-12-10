from apps.user.models import Goods, UserInfo, Collect


def collectview(userName):
    favor = Collect.objects.filter(user_name=userName)
    favor = [item.goods_id for item in favor]
    good = Goods.objects.filter(goods_id__in=favor)
    return good
