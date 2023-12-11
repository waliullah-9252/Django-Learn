from django.shortcuts import render, redirect
from .import forms 

# Create your views here.

def add_profiles(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profiles')
    else:
        profile_form = forms.ProfileForm()
    return render(request, 'profiles/add_profiles.html', {'form': profile_form})

