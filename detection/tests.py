from django.test import TestCase
from detection.models import Question
from django.utils import timezone

def insert_question():
    Question.objects.all()
    q = Question(question_text="Hi", pub_date=timezone.now())
    q.save()
