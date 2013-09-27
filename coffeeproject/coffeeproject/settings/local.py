# Settings file for local project development

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# Parse database configuration from $DATABASE_URL
import dj_database_url

# DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += \
            ("debug_toolbar.middleware.DebugToolbarMiddleware", )


# Uncomment for SQL Debug

# LOGGING = { 
#    'version': 1,
#    'disable_existing_loggers': True,
#    'formatters': {
#        'simple': {
#            'format': '%(levelname)s %(message)s',
#        },  
#    },  
#    'handlers': {
#        'console':{
#            'level':'DEBUG',
#            'class':'logging.StreamHandler',
#            'formatter': 'simple'
#        },  
#    },  
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#            'level': 'DEBUG',
#        },  
#    }   
# }
