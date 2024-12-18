from django.apps import AppConfig

class NMTSAAppConfig(AppConfig):
    name = 'nmtsa_refactor'

    def ready(self):
        print('started nmsta_cms')
        from . import signals