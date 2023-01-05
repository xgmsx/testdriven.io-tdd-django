import os

from django.conf import settings

import pytest


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", settings.DATABASES["default"]["ENGINE"]),
        "HOST": os.environ.get("DB_TEST_HOST", settings.DATABASES["default"]["HOST"]),
        "NAME": os.environ.get("DB_TEST_NAME", settings.DATABASES["default"]["NAME"]),
        "PORT": os.environ.get("DB_TEST_PORT", settings.DATABASES["default"]["PORT"]),
        "USER": os.environ.get("DB_TEST_USER", settings.DATABASES["default"]["USER"]),
        "PASSWORD": os.environ.get("DB_TEST_PASSWORD", settings.DATABASES["default"]["PASSWORD"]),
        "ATOMIC_REQUESTS": settings.DATABASES["default"]["ATOMIC_REQUESTS"],
    }
