from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .import models
from .import forms

# Create your views here.
class DetailsPostView(DetailView):
    model = models.AdminPost
    template_name = 'details_post.html'
    context_object_name = "post"
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



