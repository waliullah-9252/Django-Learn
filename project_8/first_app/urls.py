from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('changepassword/', views.change_password, name = 'changepassword'),
    path('changepassword2/', views.change_password2, name = 'changepassword2'),
    path('user_update_data/', views.user_update_data, name = 'user_update_data'),
]