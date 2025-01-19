from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegister

urlpatterns = [
    path('signup/', UserRegister.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name= 'members/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
]
