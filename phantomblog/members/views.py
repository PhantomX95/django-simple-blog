from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class UserRegister(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    