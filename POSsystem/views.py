from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
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
				return redirect("welcome")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("welcome")

def welcome(request):
	if not request.user.is_authenticated:
		return render(request, "welcome.html", {})
	else:
		return render(request, "welcome2.html", {})
