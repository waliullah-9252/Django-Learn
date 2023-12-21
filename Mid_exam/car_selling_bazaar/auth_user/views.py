from django.shortcuts import render,redirect
from .forms import SignUpForm, ChangeUserDataForm
from posts.models import AdminPost
from cars.models import BuyCars
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account was successfully created.')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'SignUp'
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(*args, **kwargs)
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                user_name = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_pass)
                if user is not None:
                    messages.success(request, 'Logged in successfully')
                    login(request, user)
                    return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
                return redirect('signup')
        else:
            login_form = AuthenticationForm()
        return render(request,'signup.html', {'form' : login_form, 'type' : 'Login'})
    else:
        return redirect('profile')

@login_required
def profile(request):
    buy_cars = BuyCars.objects.filter(place_order = request.user)
    return render(request,'profile.html', {'buy_cars' : buy_cars})


@login_required
def update_profile(request):
    if request.method == 'POST':
        update_form = ChangeUserDataForm(request.POST, instance = request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('profile')
    else:
        update_form = ChangeUserDataForm(instance = request.user)
    return render(request, 'update_profile.html', {'form': update_form})

@login_required
def password_change(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, 'Your password has been changed successfully')
            update_session_auth_hash(request, pass_change_form.user)
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(request.user)
    return render(request, 'passchange.html', {'form': pass_change_form})


def user_logout(request):
    logout(request)
    messages.success(request, 'User logged out successfully')
    return redirect('login')