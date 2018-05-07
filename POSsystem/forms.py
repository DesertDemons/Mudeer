from django import forms
from django.contrib.auth.models import User
from .models import Restaurant, Category, Item


class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = '__all__'
		exclude =['owner']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		exclude =['restaurant']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
		exclude =['category']
