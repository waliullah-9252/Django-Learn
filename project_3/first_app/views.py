from django.shortcuts import render
import datetime 

# Create your views here.

def home(request):
    d = {'author' : 'Waliullah', 'age' : 5, 'list' : ['python', 'is', 'best'], 'birthday' : datetime.datetime.now(),'value': 'hello world !', 'courses' : [
        {
            "id" : 1,
            "name" : "Python",
            "fees" : 4000,
        },
        {
            "id" : 2,
            "name" : "Django",
            "fees" : 3000,
        },
        {
            "id" : 1,
            "name" : "Cpp",
            "fees" : 2000,
        },
    ]}
    return render(request, 'first_app/home.html', d)
