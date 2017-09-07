from .common import *

INSTALLED_APPS += [ 
    'imagekit',
    'debug_toolbar',
    'django_extensions', 

]

#for debug tool-bar
INTERNAL_IPS = ["127.0.0.1"]