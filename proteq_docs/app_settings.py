from django.conf import settings

DOCUMENTATION_ROOT = getattr(settings, 'DOCUMENTATION_ROOT', '/static/docs/')
DOCUMENTATION_ACCESS_FUNCTION = getattr(settings, 'DOCUMENTATION_ACCESS_FUNCTION', None)

if not DOCUMENTATION_ROOT:
    raise Exception('Please configure DOCUMENTATION_ROOT')
if not DOCUMENTATION_ACCESS_FUNCTION:
    raise Exception('Please configure DOCUMENTATION_ACCESS_FUNCTION')

DOCUMENTATION_XSENDFILE = getattr(settings, 'DOCUMENTATION_XSENDFILE', not settings.DEBUG)