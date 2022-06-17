#App Name : Poll App
#File name : PollApp/polls/models.py
#Description : This file is for admin configuration in the poll app
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 17/06/2022

from django.contrib import admin
from .models import Question

admin.site.register(Question)