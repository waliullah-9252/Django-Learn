from django.urls import path,include
from .import views

urlpatterns = [
    # path('', views.home),
    path('', views.set_session),
    # path('get/', views.cookies_get),
    path('get/', views.session_get),
    # path('delete/', views.delete_cookies),
    path('delete/', views.session_delete),
]