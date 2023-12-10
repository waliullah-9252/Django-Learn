from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('show_data/', views.show_data, name = 'show_data'),
    path('delete_student/<int:roll>', views.delete_student, name = 'delete_student'),
]