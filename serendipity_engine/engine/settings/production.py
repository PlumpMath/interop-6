from .base import *

# fill in with local values
# these are the people who get emailed in case of critical errors;
# configurable via LOGGING below
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# fill in with local values
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# remove '*', add string(s) for the domain(s) you'll be serving the project
# from
ALLOWED_HOSTS = ['*']

# fill these in
# see https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_USE_TLS = 
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
EMAIL_PORT = 

# make these not fake
# yes, from_email is a string and interop_admins is a list of one or more 
# strings
FROM_EMAIL = 'someone@example.com'
INTEROP_ADMINS = ['self@evident.com', 'optional@additional.user']

# you will need to set an environment variable of DJANGO_SECRET_KEY
# get that from me

# Here's a sample production logging config; you may want to customize it.
# see https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(funcName)s]: %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(PROJECT_ROOT, 'logs', 'serendipity.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'brief',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}

REGISTRATION_OPEN = True
DEBUG=False