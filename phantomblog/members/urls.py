from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegister, ProfileView, EditUserAccountSettings, EditProfile

urlpatterns = [
    path('signup/', UserRegister.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name= 'members/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/profile/settings/', EditUserAccountSettings.as_view(), name='edit_user_settings'),
    path('<int:pk>/profile/edit-profile/', EditProfile.as_view(), name='edit_profile'),
]
