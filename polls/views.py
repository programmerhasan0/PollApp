# App Name : Poll App
# File name : polls/views.py
# Description : This file defines the public views of our poll app
# Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
# Date : 18/06/2022

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Choice, Question


# route hanlder :GET --> /polls
def index(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    context = {'latestQuestionList' : latestQuestionList}
    return render(request, 'polls/index.html', context)



# route handler :GET --> /polls/<id> 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

# route handler :GET --> /polls/<id>/results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})


# route handler :POST --> /polls/<id>/vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Will redisplay the voting form with an error message
        return render(request, 'polls/detail.html', {'question' : question, 'error_message' : "You didn't select a choice"})
    else : 
        selectedChoice.votes +=1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
