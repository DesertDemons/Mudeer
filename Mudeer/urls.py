
from django.conf import settings
from django.contrib import admin
from django.urls import path
from POSsystem import views 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name="welcome"),
    path('profile/', views.profile, name='profile_page'),
    path('detail/<int:restaurant_id>/', views.business_detail, name='detail'),
    path('ordering_page/<int:restaurant_id>/', views.ordering_page, name='ordering_page'),

    path('categoryDetails/<int:category_id>/', views.categoryDetails, name='categoryDetails'),
    path('addCategory/<int:restaurant_id>/', views.addCategory, name='addCategory'),
    path('update_category/<int:category_id>/', views.updateCategory, name='update_category'),
	path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),


    path('addItem/<int:category_id>/', views.addItem, name='addItem'),
    path('update_item/<int:item_id>/', views.updateItem, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    # path('welcome2/', views.welcome, name="welcome2"),

    # User authentication related URLS
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
	path('logout/', views.userlogout, name='logout'),


	path('create/', views.create, name="create_rest"),
	path('update/<int:restaurant_id>/', views.update, name="update_rest"),
	path('delete/<int:restaurant_id>/', views.delete, name="delete_rest"),


]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)