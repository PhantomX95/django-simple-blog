from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# View to display the home page
class Home(ListView):
    model = Post
    template_name = 'theblog/home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=2).order_by('-created_on')

# View to display the detail of a post
class PostDetail(DetailView):
    model = Post
    template_name = 'theblog/article_detail.html'

# View to create a new post
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'theblog/add_post.html'
    form_class = PostForm

    # Set the author of the post to the current user after creating a new post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Redirect to the detail page of the post after creating a new post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to update a post
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'theblog/update_post.html'
    form_class = UpdatePostForm

    # Set the status of the post to 'Pending' after updating a post
    def form_valid(self, form):
        form.instance.status = 1
        return super().form_valid(form)

    # Redirect to the detail page of the post after updating a post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to delete a post
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')

# Create a ListView to display the category-wise posts
class CategoryView(ListView):
    model = Post
    template_name = 'theblog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=2, category__slug=self.kwargs['category_slug']).order_by('-created_on')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category_slug']
        return context

class CategoryList(ListView):
    model = Category
    template_name = 'theblog/categories.html'
    context_object_name = 'categories'
