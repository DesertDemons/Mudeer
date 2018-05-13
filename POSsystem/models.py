from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=25)
	image = models.ImageField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	established = models.DateField(auto_now_add=True)


	def __str__(self):
		return "Name: [" + self.name + "] " + self.description



class Category(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)

	def __str__(self):
		return "Name: " + self.name 


class Item(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return "Name: " + self.name 

class OrderItem(models.Model):
	order = models.ForeignKey('Order', on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	item_total = models.DecimalField(decimal_places = 3, max_digits = 6,default=0)
	timestamp = models.DateTimeField(auto_now=True)

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.ManyToManyField(Item, through=OrderItem)
	total = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
	dinner = models.BooleanField(default=False)
	complete = models.BooleanField(default=False)


	def get_total(self):
		order_items = self.orderitem_set.all()
		total = 0
		for item in order_items:
			total += (item.quantity * item.item.price)
		return total

	
	