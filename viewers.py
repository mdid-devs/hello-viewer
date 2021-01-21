import os
import logging

from django import forms
from django.conf import settings as settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import RequestContext

from rooibos.viewers import register_viewer, Viewer
from rooibos.presentation.viewers import _get_presentation as get_presentation
from .functions import get_presentation_data

log = logging.getLogger('rooibos.hello_viewer')


class HelloViewer(Viewer):
    title = "HelloViewer"
    weight = 25
    default_options = {'notes': ''}

    def get_options_form(self):
        class OptionsForm(forms.Form):
            notes = forms.CharField(help_text="Add notes if desired",
                                    # widget=forms.Textarea
                                    )

        return OptionsForm

    def view(self, request):
        return_url = request.GET.get('next', reverse('presentation-browse'))
        presentation = self.obj
        data = get_presentation_data(presentation, request.user)
        notes = self.default_options['notes']

        if request.method == 'POST':
            options_form = self.get_options_form()
            form = options_form(request.POST)

            if form.is_valid():
                notes = form.cleaned_data['notes']
                log.debug('Hello Viewer - post received! notes: %s' % notes)
        else:
            options_form = self.get_options_form()

        tmpl = os.path.normpath(os.path.join(os.path.dirname(__file__), 'templates', 'hello.html'))
        return render(request, tmpl,
                      {'presentation': presentation,
                       'hide_default_data': presentation.hide_default_data,
                       'title': presentation.title,
                       'notes': notes,
                       'data': data,
                       'options_form': options_form,
                       'return_url': return_url,
                       })

        # TODO: put in the embed code once the normal view is working


@register_viewer('helloviewer', HelloViewer)
def helloviewer(obj, request, objid=None):
    presentation = get_presentation(obj, request, objid)
    if settings.DEBUG:
        log.debug('hello viewer - obj: %s ' % obj)
        log.debug('hello viewer - objid: %s ' % objid)
        log.debug('hello viewer - presentation: %s ' % presentation)
    return HelloViewer(presentation, request.user) if presentation else None
