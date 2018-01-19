from django.template import Template, TemplateSyntaxError
from django.template.base import Lexer, Parser
from django.template.context import Context
from django.template.engine import Engine
from django.test import TestCase

engine = Engine.get_default()


def _render_template(template):
    return Template(template).render(Context({})).strip()


class FriendlyLoadingTest(TestCase):

    def test_cannot_load_missing_taglib_using_standard_load(self):
        template = '{% load error_tags %}'
        self.assertRaises(TemplateSyntaxError, Template, template)

    def test_can_load_missing_taglib_using_friendly_load(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load error_tags %}')
        self.assertTrue(
            isinstance(Template(template), Template),
            'Expected template to initialize')

    def test_can_load_taglib_using_friendly_load(self):
        template = '{% load friendly_loader %}{% friendly_load flatpages %}'
        lexer = Lexer(template)
        parser = Parser(lexer.tokenize(), engine.template_libraries, engine.template_builtins)
        parser.parse()
        self.assertTrue(
            'get_flatpages' in parser.tags,
            'Expected flatpages taglib to load and provide the get_flatpages tag')

    def test_can_load_missing_and_existing_taglib_using_friendly_load(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load error_tags flatpages %}')
        lexer = Lexer(template)
        parser = Parser(lexer.tokenize(), engine.template_libraries, engine.template_builtins)
        parser.parse()
        self.assertTrue(
            'get_flatpages' in parser.tags,
            'Expected flatpages taglib to load and provide the get_flatpages tag')

    def test_can_load_from_taglib(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load get_flatpages from flatpages %}')
        lexer = Lexer(template)
        parser = Parser(lexer.tokenize(), engine.template_libraries, engine.template_builtins)
        parser.parse()
        self.assertTrue(
            'get_flatpages' in parser.tags,
            'Expected flatpages taglib to load and provide the get_flatpages tag')

    def test_can_load_from_missing_taglib(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load error from error_tags %}')
        lexer = Lexer(template)
        parser = Parser(lexer.tokenize(), engine.template_libraries, engine.template_builtins)
        parser.parse()
        self.assertTrue(
            isinstance(Template(template), Template),
            'Expected template to initialize')


class BaseRenderTest(TestCase):
    def assertSuccess(self, template):
        self.assertEqual(
            'SUCCESS', _render_template(template),
            'Expected template to render SUCCESS')


class HasTagTest(BaseRenderTest):

    def test_must_have_arguments(self):
        template = (
            '{% load friendly_loader %}'
            '{% if_has_tag %}FAIL{% endif_has_tag %}')
        self.assertRaises(
            TemplateSyntaxError, _render_template, template)

    def test_can_test_builtins(self):
        template = (
            '{% load friendly_loader %}'
            '{% if_has_tag now %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_missing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% if_has_tag fail %}{% fail %}'
            '{% else %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_loaded_tags(self):
        template = (
            '{% load friendly_loader flatpages %}'
            '{% if_has_tag get_flatpages %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_friendly_loaded_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% if_has_tag get_flatpages %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_multiple_existing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% if_has_tag now get_flatpages %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_both_existing_and_missing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% if_has_tag get_flatpages fail %}FAIL'
            '{% else %}SUCCESS{% endif_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_missing_tags_without_else(self):
        template = (
            '{% load friendly_loader %}'
            '{% if_has_tag fail %}FAIL{% endif_has_tag %}')
        self.assertEqual(
            '', _render_template(template),
            'Expected template to render nothing')


class NotHasTagTest(BaseRenderTest):
    def test_must_have_arguments(self):
        template = (
            '{% load friendly_loader %}'
            '{% ifnot_has_tag %}FAIL{% endifnot_has_tag %}')
        self.assertRaises(TemplateSyntaxError, _render_template, template)

    def test_can_test_builtins(self):
        template = (
            '{% load friendly_loader %}'
            '{% ifnot_has_tag now %}FAIL'
            '{% else %}SUCCESS{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_missing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% ifnot_has_tag fail %}SUCCESS'
            '{% else %}FAIL{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_loaded_tags(self):
        template = (
            '{% load friendly_loader flatpages %}'
            '{% ifnot_has_tag get_flatpages %}FAIL'
            '{% else %}SUCCESS{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_friendly_loaded_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% ifnot_has_tag get_flatpages %}FAIL'
            '{% else %}SUCCESS{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_multiple_existing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% ifnot_has_tag now get_flatpages %}FAIL'
            '{% else %}SUCCESS{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_both_existing_and_missing_tags(self):
        template = (
            '{% load friendly_loader %}'
            '{% friendly_load flatpages %}'
            '{% ifnot_has_tag get_flatpages fail %}SUCCESS'
            '{% else %}FAIL{% endifnot_has_tag %}')
        self.assertSuccess(template)

    def test_can_test_tags_without_else(self):
        template = (
            '{% load friendly_loader %}'
            '{% ifnot_has_tag now %}FAIL{% endifnot_has_tag %}')
        self.assertEqual(
            '', _render_template(template),
            'Expected template to render nothing')
