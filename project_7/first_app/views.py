from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = forms.StudnetForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = forms.StudnetForm()
    return render(request, 'first_app/home.html', {'form': form})

def show_data(request):
    show = models.StudentModel.objects.all()
    return render(request, 'first_app/show_data.html', {'show': show})


def delete_student(request,roll):
    show = models.StudentModel.objects.get(pk= roll).delete()
    return redirect('show_data')
