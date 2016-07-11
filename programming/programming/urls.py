"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from photo import views as photo_views
from blog import views as blog_views
urlpatterns = [
 url(r'^photo/(?P<pk>\d+)/$', 'photo.views.single_photo', name='view_single_photo'),
 url(r'^photo/$', 'photo.views.single_photo', name='view_single_photo'),
    url(r'^admin/', admin.site.urls),  # when 1st parameter calls, 2nd function  works
    url(r'^$', blog_views.post_list, name="home"),
    url(r'^about/$', blog_views.about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
