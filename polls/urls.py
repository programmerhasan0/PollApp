#App Name : Poll App
#File name : PollApp/urls.py
#Description : This the main router of the poll app.
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 12/06/2022
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')

    ]