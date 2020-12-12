from apps.user.models import Orderdetail,Order,Goods,UserInfo
class object:
    picture = ''
    order = Orderdetail

    def __init__(self, pic, obj):
        self.picture = pic
        self.order = obj
class view:
     Sell=[]
     Buy=[]
     Ing=[]

     def __init__(self):
         self.Ing=[]
         self.Buy=[]
         self.Sell=[]

def indexview(c_id):

    s_order=Order.objects.filter(seller_id=c_id)
    b_order=Order.objects.filter(buyer_id=c_id)
    t_order=[]
    t_view=view
    t_view.__init__(t_view)

    for entity in s_order:

         if entity.state=='finish':
             order = Orderdetail.objects.get(order_id=entity.order_id)
             picture = Goods.objects.get(goods_id=order.goods_id).picture
             s_object = object(picture, order)
             t_view.Sell.append(s_object)
         else:
            t_order.append(entity)

    for entity in b_order:

        if entity.state == 'finish':
            order = Orderdetail.objects.get(order_id=entity.order_id)
            picture = Goods.objects.get(goods_id=order.goods_id).picture
            b_object = object(picture, order)
            t_view.Buy.append(b_object)
        else:
            t_order.append(entity)

    for entity in t_order:
        order = Orderdetail.objects.get(order_id=entity.order_id)
        picture = Goods.objects.get(goods_id=order.goods_id).picture
        t_object = object(picture, order)
        t_view.Ing.append(t_object)
    return t_view

def countSelled(c_id):
       return Order.objects.filter(seller_id=c_id).count()

def not_inorder(name):
    goods=Goods.objects.filter(user_name=name)
    return goods.filter(state="not_in_order")
def getincome(c_id):
   income=0
   for order in Order.objects.filter(seller_id=c_id):
           income=income +order.cost
   return income






