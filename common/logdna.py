import os
import logging
from logdna import LogDNAHandler 

#https://github.com/logdna/python

LOGGING = {
    'version': 1,
    'handlers': {
        'logdna': {
            'level': logging.DEBUG,
            'class': 'logging.handlers.LogDNAHandler',
            'key': os.environ['LOG_DNA'],
            'options': {
                'app': 'FlaskApp',
                'env': os.environ.get('ENVIRONMENT'),
                'index_meta': True,
            },
        },
    },
    'loggers': {
        '': {
            'handlers': ['logdna'],
            'level': logging.DEBUG
        },
    },
}