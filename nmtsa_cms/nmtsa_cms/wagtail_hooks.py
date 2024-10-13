from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.admin import widgets
from home.models import file_chooser_viewset, GDrivePage, File
import nmtsa_cms.gdrive_sharing as gdrive

@hooks.register("register_admin_viewset")
def register_viewset():
    return file_chooser_viewset

def refresh_files():
    File.objects.all().delete()

    # Repopulate with mock files
    files = gdrive.get_drive_files()

    for file in files:
        File.objects.create(name=file["name"], url="http://drive.google.com/"+file["id"])

@hooks.register('before_edit_page')
def before_edit_page(request, parent_page, page_class=None):
    # Use a custom create view for the AwesomePage model
    if page_class == GDrivePage:
        print('Editing a GDrivePage')
        refresh_files()

@hooks.register('before_create_page')
def before_create_page(request, parent_page, page_class=None):
    # Use a custom create view for the AwesomePage model
    if page_class == GDrivePage:
        print('Creating a GDrivePage')
        refresh_files()

@hooks.register('register_admin_menu_item')
def manage_files_menu_item():
    return MenuItem(
        _('Manage Files'),
        reverse('manage_files'),
        icon_name='doc-full-inverse',  # You can use any available Wagtail icon or a custom one
        order=1000  # Adjust the order in which it appears
    )
