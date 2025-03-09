from django.urls import path
from .views import Home, PostDetail, CreatePost, UpdatePost, DeletePost, CategoryView, CategoryList, LikesPostView, AllPostsView, Custom404View
from django.views.generic import TemplateView
from members.views import WritersListView

handler404 = Custom404View.as_view()

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<slug:category_slug>/article/<slug:slug>/', PostDetail.as_view(), name='article_detail'),
    path('add-post/', CreatePost.as_view(), name='add_post'),
    path('article/edit/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('article/<slug:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='category_posts'),
    path('article/<int:pk>/like/', LikesPostView.as_view(), name='like_post'),
    path('contact-us/', TemplateView.as_view(template_name='theblog/contact-us.html'), name='contact-us'),
    path('about-us/', WritersListView.as_view(), name='about-us'),
    path('all-posts/', AllPostsView.as_view(), name='all-posts'),
]
