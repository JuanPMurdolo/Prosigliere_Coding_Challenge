from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import BlogPost, Comment
from .serializers import (
    BlogPostListSerializer,
    BlogPostDetailSerializer,
    CommentSerializer
)

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogPostDetailSerializer
        return BlogPostListSerializer

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        blog_post = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
        serializer.save(blog_post=blog_post)