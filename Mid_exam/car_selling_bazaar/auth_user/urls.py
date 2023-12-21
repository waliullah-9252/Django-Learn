from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view() , name = 'signup'),
    path('login/', views.user_login , name = 'login'),
    path('logout/', views.user_logout , name = 'logout'),
    path('profile/', views.profile , name = 'profile'),
    path('profile/edit/', views.update_profile , name = 'update_profile'),
    path('profile/edit/passwordchange/', views.password_change , name = 'password_change'),
]