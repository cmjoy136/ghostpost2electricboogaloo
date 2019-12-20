from django.shortcuts import render, HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ghostpost2.quickstart.serializers import *
from ghostpost2.quickstart.models import Post
from django.views import View

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote += 1
        post.save()
        return Response({'status': 'okiley dokely'})
    
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvote += 1
        post.save()
        return Response({'status': 'nokiley dokely'})

    @action(detail=False, methods=['get'])
    def filter_upvotes(self, request):
        queryset = Post.objects.order_by("-upvote")
        serializer_class = self.get_serializer(queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, methods=['get'])
    def filter_downvotes(self, request):
        queryset = Post.objects.order_by("-downvote")
        serializer_class = self.get_serializer(queryset, many=True)
        return Response(serializer_class.data)
