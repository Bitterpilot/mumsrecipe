import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Recipe


class RecipeModelTests(TestCase):

    def create_recipe(recipe_name, days):
        """
        Create a recipe with the given `recipe_name` and published the
        given number of `days` offset to now (negative for recipe published
        in the past, positive for recipe that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Recipe.objects.create(recipe_name=recipe_name, publish_date=time)


class RecipeIndexViewTests(TestCase):
    def test_no_recipe(self):
        """
        If no recipe exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('recipe:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipe are available.")
        self.assertQuerysetEqual(response.context['latest_recipe_list'], [])

    # todo ensure test is syntactically correct, then ensure method is correct
    # def test_past_recipe(self):
    #     """
    #     recipe with a publish_date in the past are displayed on the
    #     index page.
    #     """
    #     create_recipe(recipe_name="Past recipe.", days=-30)
    #     response = self.client.get(reverse('recipe:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_recipe_list'],
    #         ['<recipe: Past recipe.>']
    #     )

    def test_future_recipe(self):
        """
        recipe with a publish_date in the future aren't displayed on
        the index page.
        """
        create_recipe(recipe_name="Future recipe.", days=30)
        response = self.client.get(reverse('recipe:index'))
        self.assertContains(response, "No recipe are available.")
        self.assertQuerysetEqual(response.context['latest_recipe_list'], [])

    # todo ensure test is syntactically correct, then ensure method is correct
    # def test_future_recipe_and_past_recipe(self):
    #     """
    #     Even if both past and future recipe exist, only past recipe
    #     are displayed.
    #     """
    #     create_recipe(recipe_name="Past recipe.", days=-30)
    #     create_recipe(recipe_name="Future recipe.", days=30)
    #     response = self.client.get(reverse('recipe:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_recipe_list'],
    #         ['<recipe: Past recipe.>']
    #     )

    # todo ensure test is syntactically correct, then ensure method is correct
    # def test_two_past_recipe(self):
    #     """
    #     The recipe index page may display multiple recipe.
    #     """
    #     create_recipe(recipe_name="Past recipe 1.", days=-30)
    #     create_recipe(recipe_name="Past recipe 2.", days=-5)
    #     response = self.client.get(reverse('recipe:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_recipe_list'],
    #         ['<recipe: Past recipe 2.>', '<recipe: Past recipe 1.>']
    #     )


class RecipeDetailViewTests(TestCase):
    def test_future_recipe(self):
        """
        The detail view of a recipe with a publish_date in the future
        returns a 404 not found.
        """
        future_recipe = create_recipe(recipe_name='Future recipe.', days=5)
        url = reverse('recipe:detail', args=(future_recipe.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_recipe(self):
        """
        The detail view of a recipe with a publish_date in the past
        displays the recipe's text.
        """
        past_recipe = create_recipe(recipe_name='Past recipe.', days=-5)
        url = reverse('recipe:detail', args=(past_recipe.id,))
        response = self.client.get(url)
        self.assertContains(response, past_recipe.recipe_name)