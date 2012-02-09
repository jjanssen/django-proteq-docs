from django.conf import settings

DOCUMENTATION_ROOT = getattr(settings, 'DOCUMENTATION_ROOT', '/static/docs/')
DOCUMENTATION_ACCESS_FUNCTION = getattr(settings, 'DOCUMENTATION_ACCESS_FUNCTION', lambda user: user.is_staff)
DOCUMENTATION_XSENDFILE = getattr(settings, 'DOCUMENTATION_XSENDFILE', not settings.DEBUG)