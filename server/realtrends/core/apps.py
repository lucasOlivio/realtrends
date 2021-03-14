from django.apps import AppConfig


class CoreConfig(AppConfig):
    """ App configuration for core app. """

    name = "realtrends.core"
    verbose_name = "Core"

    def ready(self):
        try:
            import realtrends.core.signals  # noqa F401
        except ImportError:
            pass
