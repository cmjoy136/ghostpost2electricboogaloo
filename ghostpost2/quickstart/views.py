from django.shortcuts import render, HttpResponseRedirect
from rest_framework import viewsets
from ghostpost2.quickstart.serializers import *
from ghostpost2.quickstart.models import Post
from django.views import View

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
