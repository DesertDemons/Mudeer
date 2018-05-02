from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=25)
	image = models.CharField(max_length=300)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	established = models.DateField(auto_now_add=True)

	def __str__(self):
		return "Name: [" + self.name + "] " + self.description


##### Should make category model with relation of ManyToOne to Restaurant
class Category(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)

	def __str__(self):
		return "Name: " + self.name 


##### Here should be an item model with relation of ManyToOne to Restaurant


class Item(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return "Name: " + self.name 



