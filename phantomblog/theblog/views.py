from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

# View to display the home page
class Home(ListView):
    model = Post
    template_name = 'theblog/home.html'
    context_object_name = 'posts'
    paginate_by = 2

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
    form_class = UpdatePostForm

    # Redirect to the detail page of the post after updating a post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to delete a post
class DeletePost(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')

# Create a ListView to display the category-wise posts
class CategoryView(ListView):
    model = Post
    template_name = 'theblog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

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
