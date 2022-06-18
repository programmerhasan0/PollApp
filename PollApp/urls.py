
#App Name : Poll App
#File name : polls/urls.py
#Description : This the main router of the django application
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 12/06/2022


from django.contrib import admin
from django.urls import path, include
from . import _views

urlpatterns = [
    path('', _views.homePage,  name='homepage'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
