from django.shortcuts import render, redirect
from .models import Post, Portfolio_content
from blog.forms import VideoForm
# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': post_list})

def video_list(requset):
    video_list = Portfolio_content.objects.all()
    return render(request, 'blog/about_content.html',{'video_list':video_list})

def about(request):
    video_list = Portfolio_content.objects.all()
    return render(request, 'blog/about_content.html', {'video_list': video_list})

def add(request):
    if request.method == "POST":
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('add_info')
    else:
        form = VideoForm()
        print(form)
    return render(request, 'blog/add_info.html',{'form':form,})

def img_slider(request):
    return render(request, 'blog/index.html')

