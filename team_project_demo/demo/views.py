from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'demo/index.html',{})

def img_slider(request):
    return render(request, 'demo/img_slider.html',{})