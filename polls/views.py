from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("欢迎，这是主页面")


def detail(request, question_id):
    return HttpResponse("你正在看问题 %s." % question_id)


def results(request, question_id):
    return HttpResponse("你正在看问题 %s 的投票结果." % question_id)


def vote(request, question_id):
    return HttpResponse("你正在为问题 %s 投票." % question_id)
