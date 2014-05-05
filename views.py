import os

from django.shortcuts import render_to_response
from django.template import RequestContext

from rooibos.presentation.models import Presentation

from functions import get_presentation_data

# views are not necessary for a viewer, although you can use a view for testing, a special case
# or you can import rooibos.viewers.views to extend
#  viewer_shell(request, viewer, objid, template='viewers_shell.html')
#  viewer_script(request, viewer, objid)


def test(request, presentation_id):
    presentation = Presentation.objects.get(id=presentation_id)
    data = get_presentation_data(presentation, request.user)
    notes = 'A simple viewer app for demonstrating how easy it is to write a custom viewer app'

    tmpl = os.path.normpath(os.path.join(os.path.dirname(__file__), 'templates', 'hello.html'))
    return render_to_response(tmpl,
                              {'presentation': presentation,
                               'hide_default_data': presentation.hide_default_data,
                               'title': presentation.title,
                               'notes': notes,
                               'data': data,
                               },
                              context_instance=RequestContext(request))
