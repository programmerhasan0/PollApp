#App Name : Poll App
#File name : PollApp/models.py
#Description : this is the view file for the initial app.
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 18/06/2022

from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
   return render(request, 'home.html')
    