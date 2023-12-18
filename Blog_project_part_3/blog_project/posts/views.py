from django.shortcuts import render,redirect
from .import forms 
from .import models
from django.contrib.auth.decorators import login_required

# import all class based views
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'posts/add_post.html', {'form': post_form})

# create a new post using class based views
@method_decorator(login_required, name = 'dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm  # add form er kaj kortace
    template_name = 'posts/add_post.html' # fontend show kortace
    success_url = reverse_lazy('add_post') # redirect kortace 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
        
    return render(request, 'posts/add_post.html', {'form': post_form})

# edit or update a post useing class based views
@method_decorator(login_required, name = 'dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id).delete()
    return redirect('homepage')

# delete a post using class based views
@method_decorator(login_required, name = 'dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# details post using class based views
class DetalisPostView(DetailView):
    model = models.Post
    template_name = 'posts/post_details.html'
    pk_url_kwarg = 'id'

    def post(self,request, *args, **kwargs):
        commnet_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if self.request.method == 'POST':
            commnet_form = forms.CommentForm(data = self.request.POST)
            if commnet_form.is_valid():
                new_comment = commnet_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

