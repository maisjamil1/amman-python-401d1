from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializer import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions # In case you want to use IsAdmin permission

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
