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
		return render(request, "main.html", {})


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

def create(request):
	restaurant_form = RestaurantForm()
	category_form = CategoryForm()
	item_form = ItemForm()

	if request.method == "POST":
		restaurant_form = RestaurantForm(request.POST)
		category_form = CategoryForm(request.POST, prefix='category_name') 
		item_form = ItemForm(request.POST, prefix='item_name')
		if restaurant_form.is_valid() and category_form.is_valid() and item_form.is_valid():
			restaurant_form.save()
			category_form.save()
			item_form.save()

			return redirect("profile_page")
	context = {
		"restaurant_form": restaurant_form,
		"category_form": category_form,
		"item_form": item_form,
	}
	return render(request, 'create_rest.html', context)
