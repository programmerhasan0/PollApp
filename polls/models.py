
#App Name : Poll App
#File name : polls/models.py
#Description : this file defines the schema of the database for this app.
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 13/06/2022

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

