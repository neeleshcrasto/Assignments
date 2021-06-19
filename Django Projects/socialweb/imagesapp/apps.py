from django.apps import AppConfig


class ImagesappConfig(AppConfig):
    name = 'imagesapp'

    def ready(self):
        # import signal handlers
        import imagesapp.signals
