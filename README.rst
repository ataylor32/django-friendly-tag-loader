==========================
django-friendly-tag-loader
==========================

Use templatetag libraries in Django templates to optionally support features.

This app provides three template tags ``{% friendly_load %}``,
``{% if_has_tag %}`` and ``{% ifnot_has_tag %}``.

Used together you can built templates that have optional support for certain
template tags. You can use them if they are available and do something else if
they are not.

Installation
============

Add ``friendlytagloader`` to ``INSTALLED_APPS``

Usage
=====

``{% load friendly_loader %}`` in your template

Load some optional taglib ``{% friendly_load comments %}``

Or load a specific tag ``{% friendly_load cycle from future %}``

Conditionally use its tag::

  {% if_has_tag render_comment_list %}
      {% render_comment_list for obj %}
  {% else %}
      Comment support is not available
  {% endif_has_tag %}

``{% friendly_load %}`` takes multiple arguments, so loading multiple optional
template tag libraries at once is supported::

  {% friendly_load comments webdesign website_tags %}

``{% if_has_tag %}`` and ``{% ifnot_has_tag %}`` can also handle multiple
arguments.

In the case of ``if_has_tag`` this means that all given tags should be
available, so this will render nothing even though ``now`` is a built-in tag::

  {% if_has_tag now nonexisting_tag %}
    {% now 'Y' %}
  {% endif_has_tag %}

The ``ifnot_has_tag`` condition will trigger if any of the given tags is
unavailable. For example this will render the message since, even though
``now`` is a built-in tag, ``nonexisting_tag`` is not available::

  {% ifnot_has_tag now nonexisting_tag %}
    Some tags are unavailable.
  {% endifnot_has_tag %}

Credits
=======

Original Author: `Jaap Roes <https://github.com/jaap3>`_

Current Maintainer: `Adam Taylor <https://github.com/ataylor32>`_
