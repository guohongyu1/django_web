"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app import views
from novel import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html',views.index),
    url('video-(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+)).html',views.video),
    path('get_img.html', views.get_img),
    path('get_notice.html', views.get_notice),
    path('img.html',views.imgs),
    url('novel.html',v.novel)
]
