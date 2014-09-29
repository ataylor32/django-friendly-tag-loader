from django.conf.urls import patterns, url
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'$', lambda request: render(request, 'test.html'))
)
