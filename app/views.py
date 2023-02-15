from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class CrudViewSet(viewsets.ModelViewSet):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializers
     authentication_classes = [SessionAuthentication]
     permission_classes = [IsAuthenticatedOrReadOnly]
