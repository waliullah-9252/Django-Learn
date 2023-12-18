from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    # path('add/', views.add_post, name = 'add_post'),
    path('add/', views.AddPostCreateView.as_view(), name = 'add_post'), # class based views urls 
    # path('edit/<int:id>/', views.edit_post, name = 'edit_post'),
    path('edit/<int:id>/', views.EditPostView.as_view(), name = 'edit_post'), # class based views urls 
    # path('delete/<int:id>/', views.delete_post, name = 'delete_post'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name = 'delete_post'), # class based views urls 
    path('details/<int:id>/', views.DetalisPostView.as_view(), name = 'details_post'), # class based views urls 
]