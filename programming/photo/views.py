from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo
# Create your views here.

def single_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request,'photo/single.html', {'photo':photo,})

