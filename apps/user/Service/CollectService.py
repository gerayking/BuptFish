from apps.user.models import Goods, UserInfo, Collect


def collectview(userName):
    favor = Collect.objects.filter(user_name=userName)
    good = Goods.objects.filter(goods_id__in=favor)
    return good
