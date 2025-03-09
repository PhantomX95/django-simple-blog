from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, TemplateView
from django.views.generic.edit import FormMixin
from .forms import PostForm, UpdatePostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, Count

# View to display the home page
class Home(ListView):
    model = Post
    template_name = 'theblog/home.html'
    context_object_name = 'posts'
    paginate_by = 9
    search_param = 'search' # Consistent search parameter name

    # Search view
    def get_queryset(self):
        # Default ordering by created_on (newest first)
        result = super().get_queryset().filter(status=2)
        search_query = self.request.GET.get(self.search_param)
        
        # Search: Show if there's results else False
        if search_query:
            result = result.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query) | Q(category__name__icontains=search_query)
            ).distinct().order_by('-created_on')
            return result

        self.no_results = False
        return result.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get(self.search_param)
        context.update({
            'search': bool(search_query),
            'query': search_query,
            'no_results': not context['posts'].exists() if search_query else False
        })

        # Add a queryset sorted by likes (Trending)
        context['trending_posts'] = Post.objects.filter(status=2)\
        .annotate(likes_count=Count('likes'))\
        .order_by('-likes_count')
        return context

# View to display the detail of a post
class PostDetail(DetailView, FormMixin):
    model = Post
    template_name = 'theblog/article_detail.html'
    form_class = CommentForm
    context_object_name = 'post'
    
    def get_success_url(self):
        return reverse('article_detail', kwargs={'category_slug': self.object.category.slug, 'slug': self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['comment_form'] = self.get_form()
        return context
    
    # Post comment
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if not request.user.is_authenticated:
            # Redirect to login page or show an error message
            return self.form_valid(form)
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user # Set the author to logged-in user
        comment.save()
        return super().form_valid(form)

# View to create a new post
class CreatePost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'theblog/add_post.html'
    form_class = PostForm

    # Allow adding post only if the logged in user is writer
    def test_func(self):
        return self.request.user.profile.is_writer

    # Set the author of the post to the current user after creating a new post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Redirect to the detail page of the post after creating a new post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to update a post
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'theblog/update_post.html'
    form_class = UpdatePostForm

    # Allow edits only if the logged in user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user.pk == post.author.id

    # Set the status of the post to 'Pending' after updating a post
    def form_valid(self, form):
        form.instance.status = 1
        return super().form_valid(form)

    # Redirect to the detail page of the post after updating a post
    def get_success_url(self):
        return self.object.get_absolute_url()

# View to delete a post
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')
    
    # Allow deleltion only if the logged in user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user.pk == post.author.id

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
    template_name = 'theblog/home.html'
    context_object_name = 'categories'

# Likes view
class LikesPostView(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, *args, **kwargs):
        # Check if the user is authenricated
        if not self.request.user.is_authenticated:
            # Redirect to the login page and back to the same page with 'next' parameter
            return f"{reverse('login')}?next={self.request.path}"

        post_id = self.kwargs.get('pk')
        post = Post.objects.get(id=post_id)
    
        # Toggle like/unlike
        if self.request.user in post.likes.all():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        
        return reverse('article_detail', kwargs={'category_slug': post.category.slug, 'slug': post.slug}) + '#like-sec'

# All posts page
class AllPostsView(ListView):
    model = Post
    template_name = 'theblog/all-posts.html'
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_on')

# 404 PageView
class Custom404View(TemplateView):
    template_name = '404.html'
    
    def get(self, request, exception=None, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({
            'exception': str(exception) if exception else '',
            'request_path': request.path,
        })
        return self.render_to_response(context, status=404)
    