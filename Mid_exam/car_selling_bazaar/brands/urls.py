from django.urls import path,include
from .import views

urlpatterns = [
    path('brand/', views.brands_name , name = 'brands_name'),
]