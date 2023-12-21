from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from posts.models import AdminPost
from .models import BuyCars

class BuyCarNowView(View):
    template_name = 'profile.html'

    def get(self, request, id):
        buy_cars = AdminPost.objects.filter(id=id)
        user = request.user

        if buy_cars.exists():
            buy_car = AdminPost.objects.get(id=id)
            if buy_car.quantity > 0:
                buy_car.quantity = buy_car.quantity - 1
                buy_car.save()
                if BuyCars.objects.filter(admin_post=buy_car, place_order=user).exists():
                    order = BuyCars.objects.get(admin_post=buy_car, place_order=user)
                    order.quantity += 1
                    order.save()
                else:
                    BuyCars.objects.create(place_order=user, admin_post=buy_car, quantity=1)

                messages.success(request, 'Car Buy Successfully')
            else:
                messages.warning(request, 'This car is not available now')
        else:
            messages.warning(request, 'This car is not available now')

        return redirect('profile')
