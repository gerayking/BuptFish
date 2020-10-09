from django.contrib import admin

# Register your models here.
from User.models import User, Goods, Type_id, Order, Orderdetail

admin.site.register(User)
admin.site.register(Goods)
admin.site.register(Type_id)
admin.site.register(Order)
admin.site.register(Orderdetail)