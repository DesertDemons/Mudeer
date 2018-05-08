from django.contrib import admin
from .models import Restaurant, Category, Item, Order, OrderItem
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)