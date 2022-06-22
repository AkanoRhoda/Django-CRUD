from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls import url
from django import views
from django.urls import reverse_lazy

from I4G001409FXO.blog.admin import Post
# Create your views here.
def PostListView(request):
    model = Post
    
def PostCreateView(request):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    

def PostDetailView(request):
    model = Post
    
def PostUpdateView(request):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
    
def PostDeleteView(request):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")