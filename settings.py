import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key (Always keep it secret)
SECRET_KEY = ""

# Database settings
DATABASES = {
    'default': {
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 3306
    }
}
