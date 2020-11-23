from django.test import TestCase
from django.urls import reverse

from parsel import Selector


class WordCountViewURLTests(TestCase):
    def test_assert_absolute_URL_path(self):
        self.assertEqual(reverse('word_count:word_count'), '/word_count/')

    def test_site_home_redirects_to_word_count_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('word_count:word_count'))


class WordCountViewPageStructureTests(TestCase):
    def _selector(self):
        response = self.client.get(reverse('word_count:word_count'))
        content_as_str = response.content.decode(encoding='utf-8')
        return Selector(text=content_as_str)

    def test_word_count_page_has_one_form(self):
        selector = self._selector()
        found_node_list = selector.xpath('//form').getall()
        self.assertEqual(len(found_node_list), 1)

    def test_word_count_page_has_one_textarea_child_in_form(self):
        selector = self._selector()
        xpath_query = '//form//textarea'
        found_node_list = selector.xpath(xpath_query).getall()
        self.assertEqual(len(found_node_list), 1)

    def test_word_count_page_has_two_input_child_in_form(self):
        selector = self._selector()
        xpath_query = '//form//input'
        found_node_list = selector.xpath(xpath_query).getall()
        self.assertEqual(len(found_node_list), 2)

    def test_word_count_page_has_one_input_submit_child_in_form(self):
        selector = self._selector()
        xpath_query = '//form//input[@type="submit"]'
        found_node_list = selector.xpath(xpath_query).getall()
        self.assertEqual(len(found_node_list), 1)

    def test_word_count_page_has_one_input_hidden_child_in_form(self):
        selector = self._selector()
        xpath_query = '//form//input[@type="hidden"]'
        found_node_list = selector.xpath(xpath_query).getall()
        self.assertEqual(len(found_node_list), 1)

    def test_word_count_page_has_csrfmiddlewaretoken(self):
        selector = self._selector()
        xpath_query = (
            '//form//input[@type="hidden" and @name="csrfmiddlewaretoken"]'
        )
        found_node_list = selector.xpath(xpath_query).getall()
        self.assertEqual(len(found_node_list), 1)

