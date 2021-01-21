import os

HELLO_STATIC_FILES = os.path.normpath(os.path.join(os.path.dirname(__file__), 'static'))

TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(os.path.dirname(__file__), 'templates')),
)
