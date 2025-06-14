from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments', views.CommentCreateView.as_view(), name='comment-create'),
]