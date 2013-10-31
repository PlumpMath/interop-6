from .base import *

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
EMAIL_PORT = 587

FROM_EMAIL = 'andromeda.yelton@gmail.com'
INTEROP_ADMINS = ['andromeda.yelton@gmail.com']
