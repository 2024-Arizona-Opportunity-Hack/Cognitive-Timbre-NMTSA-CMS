from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.admin import widgets

@hooks.register('register_admin_menu_item')
def manage_files_menu_item():
    return MenuItem(
        _('Manage Files'),
        reverse('manage_files'),
        icon_name='doc-full-inverse',  # You can use any available Wagtail icon or a custom one
        order=1000  # Adjust the order in which it appears
    )
