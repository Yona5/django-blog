from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, 
                                  DetailView, CreateView,
                                  DeleteView, UpdateView
                                  
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

posts = [
    {
        'author': 'yonas',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2018'
    },
     {
        'author': 'john doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})