from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# create class based view all import files
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'author/add_author.html', {'form': author_form})


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'author/register.html', {'form': register_form , 'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
        else:
            messages.warning(request, 'Login information is Incorrect, please valid information or create a new account')
            return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'author/register.html', {'form' : form, 'type' : 'Login'})

# user login class based views 
class UserLoginView(LoginView):
    template_name = 'author/register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
        # return reverse_lazy('register')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    


    
@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'author/profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Acoount Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance= request.user)
    return render(request, 'author/update_profile.html', {'form': profile_form})

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'author/pass_change.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

# class based views 
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logged Out successfully')
        return reverse_lazy('user_login')