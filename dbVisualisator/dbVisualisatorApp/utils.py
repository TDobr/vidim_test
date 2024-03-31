import json
from types import SimpleNamespace

from django.utils.deprecation import MiddlewareMixin

from dbVisualisator import settings


def is_post_request(request):
    return request.method == "POST"


def is_get_request(request):
    return request.method == "GET"


def is_put_request(request):
    return request.method == "PUT"


def is_delete_request(request):
    return request.method == "DELETE"


def get_json_model_from_body(request):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode, object_hook=lambda d: SimpleNamespace(**d))


class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        if settings.DEBUG:
            setattr(request, '_dont_enforce_csrf_checks', True)
