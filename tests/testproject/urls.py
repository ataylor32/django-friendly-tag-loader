from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'$', 'django.views.generic.simple.direct_to_template', {'template': 'test.html'})
)