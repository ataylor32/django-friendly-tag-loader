from django.conf.urls import url
from django.shortcuts import render


urlpatterns = [
    url(r'$', lambda request: render(request, 'test.html'))
]
