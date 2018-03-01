# # -*- coding: utf-8 -*-

import datetime
import json

from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView


def _json_encoder(o):
    if isinstance(o, (datetime.datetime, datetime.date)):
        return o.isoformat()
    raise TypeError('%s is not JSON serializable' % o)


def to_json(data):
    return json.dumps(data, default=_json_encoder)


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def to_json_and_render(self, data):
        return self.render_to_json_response(to_json(data))

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        if context:
            for k in ['view', 'object_list']:
                if context.get(k):
                    context.pop(k)
            return context
        return {}


class JSONDetailView(JSONResponseMixin, BaseDetailView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONListView(JSONResponseMixin, BaseListView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
