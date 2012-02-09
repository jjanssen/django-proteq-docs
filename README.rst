=====================================
Django ProteQ Docs
=====================================

This `Django <http://djangoproject.com>`_ app has for purpose to integrate
protected Sphinx based proteq_docs. Based on `django-documentation 
<https://github.com/Narsil/django-documentation>`_.


Installation 
============

Installing django-proteq-docs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install into your python path using pip::

    pip install -e git+http://github.com/jjanssen/django-proteq-docs.git#egg=django-proteq-docs

Add *'proteq_docs'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'proteq_docs',
    )

Add *'url(r'^docs/', include('proteq_docs.urls', namespace='documentation')'* to your urls:: 

    urlpatterns = patterns( '',
        ....
        url(r'^docs/', include('proteq_docs.urls', namespace='documentation'),
    )

Settings
~~~~~~~~

Set up where is your documentation, and a function that has a user for argument
and returns **True** if user is allowed to see the doc. If you plan on using 
``lambda user: True``, then you probably should not be using this app, as
staticfiles would be better suited for this task. ::

    DOCUMENTATION_ROOT = '/static/docs/'
    DOCUMENTATION_ACCESS_FUNCTION = lambda user: user.is_staff

Note that django-proteq-docs serves the content via x-sendfile when DEBUG
is False, otherwise it uses 
`django.views.static.serve <https://docs.djangoproject.com/en/dev/howto/static-files/#django.views.static.serve>`_
To override use ::

    DOCUMENTATION_XSENDFILE = True