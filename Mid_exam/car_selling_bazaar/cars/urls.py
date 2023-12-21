# urls.py

from django.urls import path
from .views import BuyCarNowView

urlpatterns = [
    # other patterns
    path('buy_car/<int:id>/', BuyCarNowView.as_view(), name='buy_car'),
]
