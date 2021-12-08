from django.shortcuts import render
from blog.models import post
from rest_framework import generics
from .serializers import postSerializer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class postlist(generics.ListAPIView):
    queryset = post.objects.all()
    serializer_class = postSerializer
    http_method_names = ['get']

class postdetail(generics.ListAPIView):
    def get_queryset(self):
        slugapi = self.kwargs['slug']
        return post.objects.filter(slug=slugapi)
    serializer_class = postSerializer
    http_method_names = ['get']
