from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import TvShow

# Create your tests here.
class TvShowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.tvshow = TvShow.objects.create(
            name = 'Loki', rating = 5, rater = self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.tvshow), 'Loki 5 tester')

    def test_tvshow_name(self):
        self.assertEqual(self.tvshow.name, 'Loki')

    def test_list_page_status_code(self):
        response = self.client.get(reverse('tvshow_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        response = self.client.get(reverse('tvshow_list'))
        self.assertTemplateUsed(response, 'tvshows_list.html')

    def test_detail_page(self):
        response = self.client.get(reverse('tvshow_detail', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tvshows_detail.html')