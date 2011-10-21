from django.template import Library, TemplateSyntaxError
from django.template.defaulttags import load, LoadNode, CommentNode


register = Library()


@register.tag
def friendly_load(parser, token):
    try:
        load(parser, token)
    except TemplateSyntaxError:
        pass
    return LoadNode


@register.tag
def if_has_tag(parser, token):
    parser.skip_past('endif_has_tag')
    return CommentNode()
