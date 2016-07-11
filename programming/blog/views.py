from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': post_list})

def about(request):
    return render(request, 'blog/about_content.html')