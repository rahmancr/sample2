from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('customers', views.customer_list_view, name='customer_list'),
    ]