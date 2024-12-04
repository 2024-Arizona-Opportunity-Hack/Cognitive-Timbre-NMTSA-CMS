from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.admin import widgets
from .widgets import FileChooserWidget
from GDriveManager.models import file_chooser_viewset, GDrivePage, File
import GDriveManager.gdrive_sharing as gdrive


@hooks.register("register_admin_viewset")
def register_viewset():
    return file_chooser_viewset


@hooks.register('before_edit_user')
def before_edit_user(request, parent_page, page_class=None):
    # Use a custom create view for the AwesomePage model
    print(page_class)
    print(request)
    print(parent_page.__class__)
    # if parent_page.__class__ == GDrivePage:
    #     print('Editing a GDrivePage')
    #     # refresh_files()


# @hooks.register('before_create_page')
# def before_create_page(request, parent_page, page_class):
#     # Use a custom create view for the AwesomePage model
#     if page_class == GDrivePage:
#         print('Creating a GDrivePage')
#         refresh_files()

@hooks.register('register_admin_menu_item')
def manage_files_menu_item():
    return MenuItem(
        _('Manage Files'),
        reverse('manage_files'),
        icon_name='doc-full-inverse',  # You can use any available Wagtail icon or a custom one
        order=1000  # Adjust the order in which it appears
    )
