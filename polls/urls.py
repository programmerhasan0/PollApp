#App Name : Poll App
#File name : polls/urls.py
#Description : This the main router of the poll app.
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 12/06/2022
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')

    ]