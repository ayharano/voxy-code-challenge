from django.test import TestCase
from django.urls import reverse


class WordCountViewURLTests(TestCase):
    def test_assert_absolute_URL_path(self):
        self.assertEqual(reverse('word_count:word_count'), '/word_count/')

    def test_site_home_redirects_to_word_count_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('word_count:word_count'))
