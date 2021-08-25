# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from .models import Post
from django.urls import reverse_lazy


# Displays the list of Blog Posts on the main page
class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'

# On clicking the title of the post the details of the post will be showed
class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')