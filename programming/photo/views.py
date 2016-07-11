from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo
# Create your views here.

def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    response_text = '<p>let me show you photo No.{}</p>'
    response_text += '<p><img src="{photo_url}"/></p>'

    return HttpResponse(response_text.format(
        photo_id = photo_id,
        photo_url = photo.image_file.url
        )
    )

def single_photo(request, *args):
    return HttpResponse('let me show you photo No.{0}'.format(args[0]))
