from django.apps import AppConfig


class IndigoBylawsConfig(AppConfig):
    name = 'indigo_bylaws'
    verbose_name = 'Indigo for OpenByLaws.org.za'

    def ready(self):
        # ensure signal handlers are installed
        import indigo_bylaws.notifications  # noqa
