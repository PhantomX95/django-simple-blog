from django.urls import path
from .views import Home, PostDetail, CreatePost, UpdatePost, DeletePost, CategoryView, CategoryList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<slug:category_slug>/article/<slug:slug>/', PostDetail.as_view(), name='article_detail'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('article/edit/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('article/<slug:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='category_posts'),
]
