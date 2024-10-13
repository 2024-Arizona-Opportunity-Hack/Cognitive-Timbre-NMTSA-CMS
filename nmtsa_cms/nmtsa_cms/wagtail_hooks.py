from wagtail import hooks

from home.models import file_chooser_viewset


@hooks.register("file_chooser_viewset")
def register_viewset():
    return file_chooser_viewset