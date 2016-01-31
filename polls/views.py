# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader
# 引入模板快捷方式
from django.shortcuts import render

from django.http import Http404
# 引入404快捷方式
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Choice, Question

# Create your views here.

# 首页
def index(request):
    # 返回简单响应
    # return HttpResponse("Hello, world. Your're at the polls index.")
    
    # 显示系统中最新发布的5条question记录
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    
    # 使用模板显示页面，复杂方式
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list' : latest_question_list
    # })
    # return HttpResponse(template.render(context))
    
    # 使用模板显示页面，快捷方式
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

# 详情界面
def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # 加入404页面，复杂方式
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question' : question})
    
    # 加入404页面，快捷方式
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

# 投票结果
def results(request, question_id):
    # 显示简单界面
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    
    # 显示真实投票结果
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})
    
# 投票处理界面
def vote(request, question_id):
    # 简单显示界面
    # return HttpResponse("Your're voting on question %s." % question_id)
    
    # 处理投票结果
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 若失败则显示detail界面
        return render(request, 'polls/detail.html', {
            'question' : p, 
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 重定向到结果界面; reverse返回组装好的url字符串
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
