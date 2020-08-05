from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'debug': settings.DEBUG,
        'static': staticfiles_storage.url,
        'url': url,
    })
    return env


def url(name, **kwargs):
    return reverse(name, kwargs=kwargs.get('kwargs', kwargs))
