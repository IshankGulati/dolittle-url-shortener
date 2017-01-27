from dolittle.settings.base import *


CURRENT_ENV = 'prod'

ALLOWED_HOSTS = ['dolittle.herokuapp.com']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
