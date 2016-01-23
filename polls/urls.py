# -*- encoding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'), 
    # 详情
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'), 
    # 投票结果
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'), 
    # 投票逻辑处理
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), 
]
