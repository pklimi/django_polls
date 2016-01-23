# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 首页
def index(request):
    # 返回简单响应
    return HttpResponse("Hello, world. Your're at the polls index.")

# 详情界面
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# 投票结果
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    
# 投票处理界面
def vote(request, question_id):
    return HttpResponse("Your're voting on question %s." % question_id)
