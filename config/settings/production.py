from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your_production_secret_key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["your_production_domain.com"])

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_production_db_name",
        "USER": "your_production_db_user",
        "PASSWORD": "your_production_db_password",
        "HOST": "your_production_db_host",
        "PORT": "5432",
    }
}

STATIC_ROOT = BASE_DIR / "static"

MEDIA_ROOT = BASE_DIR / "media"
