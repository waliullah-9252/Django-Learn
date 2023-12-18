from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.

# cookies set ----
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'wali')
    # response.set_cookie('name', 'waliullah', max_age=15)
    response.set_cookie('name', 'waliullah', expires=datetime.utcnow()+timedelta(days=7))
    return response

# cookies getting ----
def cookies_get(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookies.html', {'name': name})

# delete cookies ----
def delete_cookies(request):
    response = render(request, 'delete_cookies.html')
    response.delete_cookie('name')
    return response


# seassion set 
def set_session(request):
    data = {
        'name' : 'waliullah',
        'age' : 23,
        'language' : 'bangla',
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html', )

# session get data
def session_get(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Gaust')
        # age = request.session.get('age')
        # language = request.session.get('language')
        request.session.modified = True
        return render(request, 'get_cookies.html', {'name': name,})
    else:
        return HttpResponse('Session has been expired? Please log in again')

# session delete data
def session_delete(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'delete_cookies.html')