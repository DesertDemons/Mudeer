"""Mudeer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from POSsystem import views 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.welcome, name="main"),
    path('profile/', views.profile, name='profile_page'),
    path('detail/<int:restaurant_id>/', views.business_detail, name='detail'),
    path('addCategory/<int:restaurant_id>/', views.addCategory, name='addCategory'),
    path('addItem/<int:category_id>/', views.addItem, name='addItem'),
    path('categoryDetails/<int:category_id>/', views.categoryDetails, name='categoryDetails'),
    # path('welcome2/', views.welcome, name="welcome2"),

    # User authentication related URLS
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
	path('logout/', views.userlogout, name='logout'),


	path('create/', views.create, name="create_rest"),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)