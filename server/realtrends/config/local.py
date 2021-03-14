from realtrends.config.common import *

DEBUG = True
AUTH_PASSWORD_VALIDATORS = []

# Testing
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
INSTALLED_APPS += ("django_nose",)
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
NOSE_ARGS = [
    BASE_DIR,
    "-s",
    "--nologcapture",
    "--with-coverage",
    "--with-progressive",
    "--cover-package=realtrends",
]
