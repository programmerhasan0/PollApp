#App Name : Poll App
#File name : polls/tests.py
#Description : This files represents the testing codes for the poll app
#Developer : MD HABIBUL HASAN
#Email : programmerhasan0@gmail.com
#Date : 19/06/2022


import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
    def test_wasPublishedRecentlyWithOldQuestion(self):
        # wasPublisedRrecently returens False for the question whoose pub_date is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.wasPublishedRecently(), False)

    def test_wasPublishedRecentlyWithRecentQuestion(self):
        # wasPublishedRecently() returns True for questions whose pub_date is within the last day
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.wasPublishedRecently(), True)

def create_question(question_text, days):
    #create a question with the given question_text and published the given number of 'days' offset to now (negative for questions published in the past and positive that have yet to be published).
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        # If no questions exists, In will display in appropiate message
        res = self.client.get('/polls/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No polls are available")
        self.assertQuerysetEqual(res.context['latestQuestionList'])

    def test_past_question(self):
        #Questions with the pub date in the past are displayed on the index page
        question = create_question(question_text="Past Question.", days=-30)
        res = self.client.get('/polls')
        self.assertQuerysetEqual(res.context['latestQuestionList'], [question])
    
    def test_future_question(self):
        # Question with the pub_date in the future aren't displayed on the index page
        create_question(question_text="Future question.", days=30)
        res = self.client.get('/polls/')
        self.assertContains(res, "No polls are available")
        self.assertQuerysetEqual(res.context['latestQuestionList'])

    def test_future_question_and_past_question(self):
        # Even if both past and future questions are available, only past questions will be displayed
        question = create_question(question_text="Past Question.", days=-30)
        create_question(question_text="Future Question", days=30)
        res = self.client.get('/path/')
        self.assertQuerysetEqual(res.context['latestQuestionList'], [question])

    def test_two_past_questions(self):
        # The Questions Index page may display multiple questions
        question1 = create_question(question_text="Past Question 1", days=-30)
        question2 = create_question(question_text="Past Question 2", days=-5)
        res = self.client.get('/polls/')
        self.assertQuerysetEqual(res.context['latestQuestionList'], [question2, question1])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        # The detail view of a question with a pub_date in the future returns 404 not found
        future_question = create_question(question_text="Future Question", days=5)
        url = reverse('<int:pk>/', args=(future_question.id))
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_past_question(self):
        # The detail view of a question with a pub_date in the past displays the questions text
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse('<int:pk>/', args=(past_question.id))
        res = self.client.get(url)
        self.assertContains(res, past_question.question_text)


