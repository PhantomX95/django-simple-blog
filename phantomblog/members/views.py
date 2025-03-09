from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm, UserForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from theblog.models import Post

class UserRegister(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Your account was created successfully. You can now log in.'

class ProfileView(DetailView):
    model = Profile
    template_name = 'members/profile.html'
    context_object_name = 'profile'
    
    def get_object(self):
        user_pk = self.kwargs.get('pk')
        return User.objects.get(pk=user_pk).profile
    
    # Show the author's posts on profile page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object().user
        context['posts'] = Post.objects.filter(author=user, status=2).order_by('-created_on')
        return context

class EditUserAccountSettings(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'members/edit_settings.html'
    form_class = UserForm
    
    def test_func(self):
        # Ensure only the user can edit their own settings
        return self.request.user.pk == self.kwargs['pk']
    
    def get_success_url(self):
        # Redirect to the user's profile page after successful edit
        return reverse('profile', kwargs={'pk':self.object.pk})
    
class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'members/edit_profile.html'
    form_class = ProfileForm

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class CustomLoginView(LoginView):
    template_name = 'members/login.html'
    
    # If 'next' is provided in the query parameters, redirect to that URL
    def get_success_url(self):
        return self.request.GET.get('next')

class CustomSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next')
        if next_url:
            self.success_url = next_url
        return response

class WritersListView(ListView):
    model = Profile
    template_name = 'theblog/about-us.html'
    context_object_name = 'writers'

    def get_queryset(self):
        return Profile.objects.filter(is_writer=True)