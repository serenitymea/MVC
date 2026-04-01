from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question, Choice


class QuestionModelTest(TestCase):

    def test_create_question(self):
        q = Question.objects.create(
            question_text="t question",
            pub_date=timezone.make_aware(datetime.datetime(2024, 1, 1))
        )
        self.assertEqual(q.question_text, "t question")


class ChoiceModelTest(TestCase):

    def test_create_choice(self):
        q = Question.objects.create(
            question_text="t question",
            pub_date=timezone.make_aware(datetime.datetime(2024, 1, 1))
        )

        c = Choice.objects.create(
            question=q,
            choice_text="t choice",
            votes=0
        )

        self.assertEqual(c.choice_text, "t choice")
        self.assertEqual(c.votes, 0)