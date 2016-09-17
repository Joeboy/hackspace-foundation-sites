"""
WSGI config for lhs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

sys.path = [
        '/var/www/hackspace-foundation-sites/',
        '/var/www/hackspace-foundation-sites/env/lib/python3.4/site-packages/',
    ] + sys.path


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lhs.settings")

application = get_wsgi_application()
