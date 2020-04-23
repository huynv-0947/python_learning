from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from django.utils import timezone
import datetime, pdb

from .models import Question

class QuestionModelTest(TestCase):
  def test_was_published_recently_with_future_question(self):
    time_in_future = timezone.now() + datetime.timedelta(days = 10)
    question = Question(publish_date = time_in_future)

    self.assertIs(question.was_published_recently(), False)

class QuestionIndexViewTest(TestCase):
  def test_with_no_question(self):
    response = self.client.get(reverse('polls:index'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No question!")
    self.assertQuerysetEqual(response.context['questions'], [])

  def test_with_one_question(self):
    Question.objects.create(text = 'Your name?', publish_date = timezone.now())

    response = self.client.get(reverse('polls:index'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Your name?")
    self.assertQuerysetEqual(response.context['questions'], ['<Question: Your name?>'])
