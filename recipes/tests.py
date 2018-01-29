import datetime

from django.test import TestCase
from django.utils import timezone


from .models import Recipe, Ingredient


class RecipeModelTest(TestCase):

    def test_was_published_recently(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Recipe(publish_date=time)
        self.assertIs(future_question.was_published_recently(), False)
