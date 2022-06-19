# App Name : Poll App
# File name : polls/views.py
# Description : This file defines the public views of our poll app
# Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
# Date : 18/06/2022

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


# route hanlder :GET --> /polls
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]


# route handler :GET --> /polls/<id> 
class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question
    def get_queryset(self):
        # Exclude any question that aren't published yet
        return Question.objects.filter(pub_date__lte=timezone.now())

# route handler :GET --> /polls/<id>/results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



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
