from apps.user.models import Order, Orderdetail




def getOrderById(t_orderId):
        order=Order.objects.get(order_id=t_orderId)
        orderdetails = Orderdetail.objects.get(order_id=t_orderId)
        print(t_orderId)
        return order,orderdetails

def getOrderByUserId(self, userId: int):
        """
        获取用户的订单
        userId : 用户Id
        """
        orders = Order.objects.filter(buyer_id=userId)
        ordersidlist = [item.order_id for item in orders]
        orderdetails = Orderdetail.objects.filter(order_id=ordersidlist)
        return orders, orderdetails

def updateOrder(order:Order):
        order.save()
        """
        更新用户订单
        orderId : 订单Id
        """


