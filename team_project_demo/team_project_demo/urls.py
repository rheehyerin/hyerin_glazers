"""team_project_demo URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from demo import views as demo_views


urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', include('demo.urls', namespace='demo')),
    url(r'^img_slider/$', demo_views.img_slider),
    url(r'^sliderEx/$', demo_views.slider_ex),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

