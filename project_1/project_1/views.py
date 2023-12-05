
from django.http import HttpResponse

def home(request):
    return HttpResponse('This is my home page here!')

def contact(resquest):
    return HttpResponse('This is my contact page here!')


