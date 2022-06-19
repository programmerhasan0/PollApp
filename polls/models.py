#App Name : Poll App
#File name : polls/models.py
#Description : this file defines the schema of the database for this app.
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 13/06/2022

from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) :
        return self.question_text

    def wasPublishedRecently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

