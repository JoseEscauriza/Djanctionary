import environ
from .base import *

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
SECRET_KEY = env.str("secret_dev_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("dbname"),
        "USER": env.str("db_user"),
        "PASSWORD": env.str("db_password"),
        "HOST": env.str("db_host"),
        "PORT": env.str("db_port")
    }
}
