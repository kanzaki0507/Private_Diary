from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECRET_KEY = '+#=bn4d2+f9ung*y-(ku(co^+nmx$=*n5ufv5w4wqm4zn7se%e'

ALLOWED_HOST = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'Loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッター設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
