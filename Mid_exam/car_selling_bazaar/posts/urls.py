from django.urls import path,include
from .import views

urlpatterns = [
    path('details/<int:id>', views.DetailsPostView.as_view(), name = 'details'),
]