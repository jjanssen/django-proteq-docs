# Create your views here.
import mimetypes
import app_settings

from django.http import HttpResponse, Http404
from django.views.static import serve


def documentation(request, path):
    if not app_settings.DOCUMENTATION_ACCESS_FUNCTION(request.user):
        raise Http404
    if not app_settings.DOCUMENTATION_XSENDFILE:
        return serve(request, path, app_settings.DOCUMENTATION_HTML_ROOT)
    mimetype, encoding = mimetypes.guess_type(path)
    response = HttpResponse(mimetype=mimetype)

    response['Content-Encoding'] = encoding
    response['Content-Disposition'] = ''
    response['X-Sendfile'] = ''.join([app_settings.DOCUMENTATION_HTML_ROOT, path])
    return response
