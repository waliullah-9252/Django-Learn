from django.shortcuts import render

from .froms import contactForm, StudentForm, PasswordValidationProject


def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'first_app/about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'first_app/about.html')

def submit_form(request):
    return render(request, 'first_app/form.html')


# django built in forms function
def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file_upload']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'first_app/django_form.html', {'form': form})


# student forms functions with validation 

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'first_app/django_form.html', {'form':form})


# password validation forms functions

def password_validation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = PasswordValidationProject()
    return render(request, 'first_app/django_form.html', {'form':form})
