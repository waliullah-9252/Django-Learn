from django.shortcuts import render
from posts.models import AdminPost
from brands.models import BrandModel

def home(request, brand_slug=None):
    data = AdminPost.objects.all()
    if brand_slug is not None:
        brand = BrandModel.objects.get(slug = brand_slug)
        data = AdminPost.objects.filter(brand = brand)
    brands = BrandModel.objects.all()
    return render(request,'home.html', {'data': data, 'brand': brands})