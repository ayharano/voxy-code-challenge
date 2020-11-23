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


class WordCountViewPageResponseTests(TestCase):

    def _get_csrfmiddlewaretoken(self):
        response = self.client.get(reverse('word_count:word_count'))
        content_as_str = response.content.decode(encoding='utf-8')
        selector = Selector(text=content_as_str)
        xpath_query = (
            '//form/input[@type="hidden" and @name="csrfmiddlewaretoken"]'
            '/@value'
        )
        return selector.xpath(xpath_query).get()

    def test_submit_empty_textbox_status_code_400(self):
        csrfmiddlewaretoken = self._get_csrfmiddlewaretoken()
        after_post = self.client.post(
            reverse('word_count:word_count'),
            {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "textbox": "",
            }
        )
        self.assertEqual(after_post.status_code, 400)

    def test_submit_invisible_char_textbox_status_code_400(self):
        csrfmiddlewaretoken = self._get_csrfmiddlewaretoken()
        after_post = self.client.post(
            reverse('word_count:word_count'),
            {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "textbox": "  \t \r\n ",
            }
        )
        self.assertEqual(after_post.status_code, 400)

    def test_submit_usual_text_in_textbox_correct_word_count(self):
        csrfmiddlewaretoken = self._get_csrfmiddlewaretoken()
        after_post = self.client.post(
            reverse('word_count:word_count'),
            {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "textbox": "\r\nHey!\r\n",
            }
        )
        self.assertEqual(after_post.status_code, 200)
        self.assertEqual(after_post.content, r"Found a word in text.")

    def test_submit_usual_text_in_textbox_correct_word_count(self):
        csrfmiddlewaretoken = self._get_csrfmiddlewaretoken()
        after_post = self.client.post(
            reverse('word_count:word_count'),
            {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "textbox": """Meet Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by
experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app
 without needing to reinvent the wheel. It’s free and open source.""",
            }
        )
        self.assertEqual(after_post.status_code, 200)
        self.assertEqual(after_post.content, b"Found 51 words in text.")
