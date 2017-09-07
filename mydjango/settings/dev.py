from .common import *

INSTALLED_APPS += [ 
    'imagekit',
    'debug_toolbar',
    'django_extensions', 

]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

#for debug tool-bar
INTERNAL_IPS = ["127.0.0.1"]