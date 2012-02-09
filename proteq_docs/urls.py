from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('proteq_docs.views',
    url(r'^(?P<path>.*)$', 'documentation', name='index'),
)