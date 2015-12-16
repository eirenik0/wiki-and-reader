# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''

from .common import *  # noqa

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='wiki_allatra_club <noreply@wiki.allatra.club>')

EMAIL_HOST = env("DJANGO_EMAIL_HOST", default='smtp.gmail.com')
EMAIL_HOST_PASSWORD = env("GMAIL_PASSWORD", default="schambala2012")
EMAIL_HOST_USER = env('GMAIL_USERNAME', default="wiki.allatra.club@gmail.com")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[wiki.allatra.club] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL")

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': env("DJANGO_CACHE_URL", default="memcache://127.0.0.1:11211")
}


