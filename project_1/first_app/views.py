from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse('This is first app page here!')

def courses(request):
    return HttpResponse('This is first app / course page here!')

def about(request):
    return HttpResponse('This is first app / about page here!')