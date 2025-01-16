from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

class Home(ListView):
    model = Post
    template_name = 'theblog/home.html'

    def get_queryset(self):
        return Post.objects.filter(status=2).order_by('-created_on')

class PostDetail(DetailView):
    model = Post
    template_name = 'theblog/article_detail.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'theblog/add_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Post
    template_name = 'theblog/update_post.html'
    fields = ['title', 'slug', 'title_tag', 'content', 'img', 'status']

class DeletePost(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')