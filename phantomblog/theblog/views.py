from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# View to display the home page
class Home(ListView):
    model = Post
    template_name = 'theblog/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=2).order_by('-created_on')

# View to display the detail of a post
class PostDetail(DetailView):
    model = Post
    template_name = 'theblog/article_detail.html'

# View to create a new post
class CreatePost(CreateView):
    model = Post
    template_name = 'theblog/add_post.html'
    form_class = PostForm

    # Redirect to the detail page of the post after creating a new post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to update a post
class UpdatePost(UpdateView):
    model = Post
    template_name = 'theblog/update_post.html'
    form_class = PostForm

    # Redirect to the detail page of the post after updating a post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to delete a post
class DeletePost(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')
