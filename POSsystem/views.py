from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, RestaurantForm, CategoryForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from .models import Restaurant, Category, Item 

# Create your views here.


def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user = form.save(commit=False)
			my_user = user.username
			my_password = user.password
			user.set_password(user.password)
			user.save()
			
			login(request, user)
			return redirect("welcome")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("profile_page")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("main")

def welcome(request):
	if not request.user.is_authenticated:
		return render(request, "main.html", {})
	else:
		return render(request, "profile_page.html", {})


def profile(request):
	restaurants = Restaurant.objects.all()
	# order objects by name and date of  established
	restaurants = restaurants.order_by('name', 'established')
	# for search functionality 
	query = request.GET.get('q')
	if query:
		restaurants = restaurants.filter(name__contains=query)
	# if user not logged in he can't see the profile page
	if request.user.is_anonymous:
		return redirect('login')

	context = {
		"restaurants": restaurants,
		}
	return render(request, 'profile_page.html', context)

def business_detail(request, restaurant_id):
	# To get the restaurant you choose
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)

	#### This is for html page to get categories and items from restaurant
	# for category in restaurant_obj.category_set.all():
	# 	for item in category.item_set.all():

	context = {
		"restaurant_obj": restaurant_obj,
	}
	return render(request, 'detail.html', context)



def create(request):
	restaurant_form = RestaurantForm()
	# category_form = CategoryForm()
	# item_form = ItemForm()

	if request.method == "POST":
		restaurant_form = RestaurantForm(request.POST)
		### These prints are to test which button was clicked!! yes we are watching YOU!!!
		# print (request.POST.get("save"))
		# print (request.POST.get("create"))
		# category_form = CategoryForm(request.POST, prefix='category_name') 
		# item_form = ItemForm(request.POST, prefix='item_name')
		if restaurant_form.is_valid():# and category_form.is_valid() and item_form.is_valid():
			restaurant = restaurant_form.save(commit=False)
			restaurant.owner=request.user
			restaurant.save()
			# category_form.save()
			# item_form.save()

			return redirect("profile_page")
	context = {
		"restaurant_form": restaurant_form,
		# "category_form": category_form,
		# "item_form": item_form,
	}
	return render(request, 'create_rest.html', context)



def addCategory(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	category_form = CategoryForm()
	if request.method == "POST":
		category_form = CategoryForm(request.POST)
		
		
		if category_form.is_valid():
			category = category_form.save(commit=False)
			category.restaurant = restaurant_obj
			category.save()
			if request.POST.get("save"):
			# But if the user clicked on "save and add another" button he will have another category form to fill
				return redirect("addCategory", restaurant_id=restaurant_obj.id)
			else:
			# if user clicked on "save" button he will be redirected to the restaurant detail page
				return redirect("detail",restaurant_id=restaurant_obj.id)
		
		

	context = {
		"restaurant_obj": restaurant_obj,
		"category_form": category_form,
	}
	return render(request, 'addCategory.html', context)


def categoryDetails(request, category_id):
	context = {
		"category": Category.objects.get(id=category_id)
		}
	return render(request, 'categoryDetails.html', context) 



def addItem(request, category_id):
	category_obj = Category.objects.get(id=category_id)
	item_form = ItemForm()
	if request.method == "POST":
		item_form = ItemForm(request.POST)
		
		
		if item_form.is_valid():
			item = item_form.save(commit=False)
			item.category = category_obj
			item.save()
			if request.POST.get("save"):
			# But if the user clicked on "save and add another" button he will have another item form to fill
				return redirect("addItem", category_id=category_obj.id)
			else:
			# if user clicked on "save" button he will be redirected to the restaurant detail page
				return redirect("this should be page of category details",category_id=category_obj.id)
		
		

	context = {
		"category_obj": category_obj,
		"item_form": item_form,
	}
	return render(request, 'addItem.html', context)

