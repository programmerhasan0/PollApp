# App Name : Poll App
# File name : polls/views.py
# Description : This file defines the public views of our poll app
# Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
# Date : 18/06/2022

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


# route hanlder --> /polls
def index(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    context = {'latestQuestionList' : latestQuestionList}
    return render(request, 'polls/index.html', context)



# route handler --> /polls/<id> 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
