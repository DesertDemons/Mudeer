from django.contrib import admin
from .models import Restaurant, Category, Item
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Item)