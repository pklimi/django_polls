# -*- encoding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # 目录列表
    url(r'^dirlist/$', views.dirlist, name='dirlist'),
    # 文件列表
    url(r'^(?P<dir_id>[0-9]+)/filelist/$', views.filelist, name='filelist'), 
]
