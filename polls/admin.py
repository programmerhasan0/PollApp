# App Name : Poll App
# File name : PollApp/polls/models.py
# Description : This file is for admin configuration in the poll app
# Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
# Date : 17/06/2022

from django.contrib import admin
from .models import Question, Choice


admin.AdminSite.site_header = "Poll App Admin"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information", {'fields': ['question_text']}),
        ("Date Information", {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'wasPublishedRecently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
