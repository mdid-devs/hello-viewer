from django.conf.urls import patterns, url
from django.conf import settings
from views import *

# see views.py (view handling for viewers is mostly by [app].viewers.py and rooibos.viewers.py

urlpatterns = patterns('',
                       # you can test the viewer via http://127.0.0.1:8000/hello-viewer/5436/
                       # where 5436 is a presentation_id -- comment out if undesired
                       url(r'^(?P<presentation_id>\d+)/$', test, name='test'),
                       # for development only - disable for production
                       # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                       #     {'document_root': settings.HELLO_STATIC_FILES, 'show_indexes': True},
                       #     name='hello_static'),
                       )