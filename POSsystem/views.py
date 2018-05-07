from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, RestaurantForm, CategoryForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from .models import Restaurant, Category, Item 
from django.http import Http404



def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
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
    return redirect("welcome")

def welcome(request):
	if not request.user.is_authenticated:
		return render(request, "main.html", {})
	else:
		return redirect("profile_page")


def profile(request):
	restaurants = Restaurant.objects.all()
	restaurants = restaurants.order_by('name', 'established')
	owner_name = request.user
	if not(request.user.is_staff):
		restaurants = restaurants.filter(owner=owner_name)
	query = request.GET.get('q')
	if query:
		restaurants = restaurants.filter(name__contains=query)
	if request.user.is_anonymous:
		return redirect('login')

	context = {
		"restaurants": restaurants,
		}
	return render(request, 'profile_page.html', context)

def business_detail(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	context = {
		"restaurant_obj": restaurant_obj,
	}
	return render(request, 'detail.html', context)



def create(request):
	restaurant_form = RestaurantForm()
	if request.method == "POST":
		restaurant_form = RestaurantForm(request.POST)
		if restaurant_form.is_valid():
			restaurant = restaurant_form.save(commit=False)
			restaurant.owner=request.user
			restaurant.save()
			

			return redirect("profile_page")
	context = {
		"restaurant_form": restaurant_form,
		
	}
	return render(request, 'create_rest.html', context)

def update(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	if not(request.user.is_staff or request.user==restaurant_obj.owner):
		# return HttpResponse("<h1>Error you are not the owner of the restaurant or staff member</h1>")
		raise Http404("You don't have permission")
	form = RestaurantForm(instance=restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance=restaurant_obj)
		if request.POST.get("cancle"):
				return redirect("profile_page")
		else:
			form.is_valid()
			form.save()
			return redirect("profile_page")
	context = {
		"form": form,
		"restaurant_obj": restaurant_obj,
	}
	return render(request, 'update_rest.html', context)

def delete(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	if not (request.user.is_staff or request.user==restaurant_obj.owner):
		# return HttpResponse("<h1>You don't have the permission to delete the restaurant</h1>")
		raise Http404("You don't have permission")
	Restaurant.objects.get(id=restaurant_id).delete()
	
	return redirect("profile_page")


def categoryDetails(request, category_id):
	context = {
		"category": Category.objects.get(id=category_id)
		}
	return render(request, 'categoryDetails.html', context) 



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
				return redirect("addCategory", restaurant_id=restaurant_obj.id)
			else:
				return redirect("detail",restaurant_id=restaurant_obj.id)
		
	context = {
		"restaurant_obj": restaurant_obj,
		"category_form": category_form,
	}
	return render(request, 'addCategory.html', context)

def updateCategory(request, category_id):
	category_obj = Category.objects.get(id=category_id)
	if not(request.user.is_staff or request.user==category_obj.restaurant.owner):
		# return HttpResponse("<h1>Error you are not the owner of the restaurant or staff member</h1>")
		raise Http404("You don't have permission")
	form = CategoryForm(instance=category_obj)
	if request.method == "POST":
		form = CategoryForm(request.POST, instance=category_obj)
		if request.POST.get("cancle"):
				return redirect("detail",restaurant_id=category_obj.restaurant.id)
		else:
			form.is_valid()
			form.save()
			return redirect("detail",restaurant_id=category_obj.restaurant.id)
	context = {
		"form": form,
		"category_obj": category_obj,
	}
	return render(request, 'update_category.html', context)

def delete_category(request, category_id):
	category_obj = Category.objects.get(id=category_id)
	if not (request.user.is_staff or request.user==category_obj.restaurant.owner):
		# return HttpResponse("<h1>You don't have the permission to delete the restaurant</h1>")
		raise Http404("You don't have permission")
	Category.objects.get(id=category_id).delete()
	
	return redirect("detail",restaurant_id=category_obj.restaurant.id)


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
				return redirect("addItem", category_id=category_obj.id)
			else:
				return redirect("detail",restaurant_id=category_obj.restaurant.id)

	
	context = {
		"category_obj": category_obj,
		"item_form": item_form,
	}
	return render(request, 'addItem.html', context)

def updateItem(request, item_id):
	item_obj = Item.objects.get(id=item_id)
	if not(request.user.is_staff or request.user==item_obj.category.restaurant.owner):
		# return HttpResponse("<h1>Error you are not the owner of the restaurant or staff member</h1>")
		raise Http404("You don't have permission")
	form = ItemForm(instance=item_obj)
	if request.method == "POST":
		form = ItemForm(request.POST, instance=item_obj)
		if request.POST.get("cancle"):
				return redirect("detail",restaurant_id=item_obj.category.restaurant.id)
		else:
			form.is_valid()
			form.save()
			return redirect("detail",restaurant_id=item_obj.category.restaurant.id)
	context = {
		"form": form,
		"item_obj": item_obj,
	}
	return render(request, 'update_item.html', context)

def delete_item(request, item_id):
	item_obj = Item.objects.get(id=item_id)
	if not (request.user.is_staff or request.user==item_obj.item.restaurant.owner):
		# return HttpResponse("<h1>You don't have the permission to delete the restaurant</h1>")
		raise Http404("You don't have permission")
	Item.objects.get(id=item_id).delete()
	
	return redirect("detail",restaurant_id=item_obj.category.restaurant.id)


def ordering_page(request,restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	context = {
		"restaurant": restaurant_obj,
	}
	return render(request, 'ordering_page.html', context)




