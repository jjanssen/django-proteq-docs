from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('documentation.views',
    url(r'^(?P<path>.*)$', 'documentation', name='index'),
)