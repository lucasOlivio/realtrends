import os

from .common import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    default="LtNmDzeNiKbTodtt3otJQSHj19cCi6QpOjhb4tRghXnkfDPIp4q4UHGSqZ3qKCrk",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# Your stuff...
# ------------------------------------------------------------------------------
