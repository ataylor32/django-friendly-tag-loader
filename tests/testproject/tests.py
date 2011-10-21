"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.template import Lexer, Parser, StringOrigin, Template, TemplateSyntaxError
from django.template.context import Context
from django.test import TestCase


def _render_template(template):
    return Template(template).render(Context({})).strip()


class FriendlyLoadingTest(TestCase):

    def test_cannot_load_non_existing_taglib_using_standard_load(self):
        template = '{% load error_tags %}'
        self.assertRaises(TemplateSyntaxError, Template, template)

    def test_can_load_non_existing_taglib_using_friendly_load(self):
        template = '{% load friendly_loader %}{% friendly_load error_tags %}'
        self.assertTrue(isinstance(Template(template), Template),
            'Expected template to initialize')

    def test_can_load_existing_taglib_using_friendly_load(self):
        template = '{% load friendly_loader %}{% friendly_load webdesign %}'
        lexer = Lexer(template, StringOrigin(template))
        parser = Parser(lexer.tokenize())
        parser.parse()
        self.assertTrue('lorem' in parser.tags,
            'Expected webdesign taglib to load and provide the lorem tag')

    def test_can_load_both_nonexisting_and_existing_taglib_using_friendly_load(self):
        template = '{% load friendly_loader %}{% friendly_load error_tags webdesign %}'
        lexer = Lexer(template, StringOrigin(template))
        parser = Parser(lexer.tokenize())
        parser.parse()
        self.assertTrue('lorem' in parser.tags,
            'Expected webdesign taglib to load and provide the lorem tag')


class HasTagTest(TestCase):

    def test_must_have_arguments(self):
        template = '''
        {% load friendly_loader %}
        {% if_has_tag %}FAIL{% endif_has_tag %}'''
        self.assertRaises(TemplateSyntaxError, _render_template, template)

    def test_can_test_builtins(self):
        template = '''
        {% load friendly_loader %}
        {% if_has_tag now %}SUCCESS{% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_nonexisting_tags(self):
        template = '''
        {% load friendly_loader %}
        {% if_has_tag fail %}
            {% fail %}
        {% else %}
            SUCCESS
        {% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_loaded_tags(self):
        template = '''
        {% load friendly_loader webdesign %}
        {% if_has_tag lorem %}SUCCESS{% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_friendly_loaded_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% if_has_tag lorem %}SUCCESS{% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_multiple_existing_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% if_has_tag now lorem %}SUCCESS{% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_both_existing_and_nonexisting_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% if_has_tag lorem fail %}
            {% fail %}
        {% else %}
            SUCCESS
        {% endif_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_not_having_tag_renders_nothing(self):
        template = '''
        {% load friendly_loader %}
        {% if_has_tag fail %}{% fail %}{% endif_has_tag %}'''
        self.assertEqual('', _render_template(template),
                         'Expected template to render nothing')


class NotHasTagTest(TestCase):

    def test_must_have_arguments(self):
        template = '''
        {% load friendly_loader %}
        {% ifnot_has_tag %}FAIL{% endifnot_has_tag %}'''
        self.assertRaises(TemplateSyntaxError, _render_template, template)

    def test_can_test_builtins(self):
        template = '''
        {% load friendly_loader %}
        {% ifnot_has_tag now %}
            FAIL
        {% else %}
            SUCCESS
        {% endifnot_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_nonexisting_tags(self):
        template = '''
        {% load friendly_loader %}
        {% ifnot_has_tag fail %}
            SUCCESS
        {% else %}
            {% fail %}
        {% endifnot_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_loaded_tags(self):
        template = '''
        {% load friendly_loader webdesign %}
        {% ifnot_has_tag lorem %}
            FAIL
        {% else %}
            SUCCESS
        {% endifnot_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_friendly_loaded_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% ifnot_has_tag lorem %}
            FAIL
        {% else %}
            SUCCESS
        {% endifnot_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_multiple_existing_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% ifnot_has_tag now lorem %}
            FAIL
        {% else %}
            SUCCESS
        {% endifnot_has_tag %}
        '''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_can_test_both_existing_and_nonexisting_tags(self):
        template = '''
        {% load friendly_loader %}
        {% friendly_load webdesign %}
        {% ifnot_has_tag lorem fail %}
            SUCCESS
        {% else %}
            {% fail %}
        {% endifnot_has_tag %}'''
        self.assertEqual('SUCCESS', _render_template(template),
                         'Expected template to render SUCCESS')

    def test_having_tag_renders_nothing(self):
        template = '''
        {% load friendly_loader %}
        {% ifnot_has_tag now %}{% now 'Y' %}{% endifnot_has_tag %}'''
        self.assertEqual('', _render_template(template),
                         'Expected template to render nothing')

