from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('mens_product/', views.mens_product),
    path('womens_product/', views.womens_product),
    path('kids_product/', views.kids_product),
    path('view_product/', views.view_product),
    path('my_cart/', views.my_cart),
    path('my_orders/', views.my_orders),
    path('my_profile/', views.my_profile),
    path('contact_us/', views.contact_us),
    path('sign_up/', views.sign_up),
    path('sign_in/', views.sign_in),
    path('signin/', views.signin),
    path('log_out/', views.log_out),
]