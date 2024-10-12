from django.apps import AppConfig

class NMTSAAppConfig(AppConfig):
    name = 'nmtsa_cms'

    def ready(self):
        print('started nmsta_cms')
        import nmtsa_cms.signals