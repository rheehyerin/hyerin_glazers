from django.conf import settings
from django.conf.urls import url

from demo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^img_slider/$', views.img_slider, name='img_slider'),
]