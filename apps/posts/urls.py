# apps/posts/urls.py

from django.urls import path
from apps.posts.views import PostListView,  PostCreateView, like_post,post_comment, post_detail

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='newsfeed'),  # Newsfeed page
    path('create/', PostCreateView.as_view(), name='post_create'),  # Create post page
    path('<int:post_id>/', post_detail, name='post_detail'),  # Post detail
    path('like/<int:post_id>/', like_post, name='like_post'),  # Like functionality
   path('comment/<int:post_id>/', post_comment, name='post_comment'),
   
]
