import requests
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import Group, User
from django.dispatch import receiver
from django.core.signals import request_finished

import GDriveManager.gdrive_sharing as gdrive
from GDriveManager.models import GDrivePage

test_dict = {
    'Moderators': [],
    'Editors': [],
    'admin': [],
}


# TODO: handle sharing with just a single person

@receiver(post_save, sender=GDrivePage)
def gdrive_page_save_handler(sender, instance, created, **kwargs):
    if created:
        print(f'New GDrivePage created: {instance}')
        # Add any additional logic for when a new GDrivePage is created
    else:
        print('GDrivePage updated')
        groups = instance.g_drive_groups.all()
        for group in groups:
            print(f'Group: {group.group.name}')
            users = group.group.user_set.all()
            for user in users:
                for file in instance.g_drive_page_files.all():
                    print(f'Sharing file {file.file.file_id} with {user.email}')
                    gdrive.share_item(file.file.file_id, user.email)


@receiver(m2m_changed, sender=User.groups.through)
def role_change_handler(sender, instance, action, pk_set, **kwargs):
    if action == "post_remove":
        removed_groups = Group.objects.filter(pk__in=pk_set)

        # Iterate over removed groups,
        for group in removed_groups:
            print(f'Group removed: {group.name}')

            # Iterate over files that a group has access to
            gdrive_pages = GDrivePage.objects.filter(g_drive_groups__group=group)
            for gdrive_page in gdrive_pages:
                for file in gdrive_page.g_drive_page_files.all():
                    print(f'Unsharing file {file.file.file_id} with {instance.email}')
                    # Get permissions for the file
                    permissions = gdrive.list_perms(file.file.file_id)

                    print(permissions)

                    permissions = filter(lambda x: x.get('emailAddress') == instance.email,
                                         permissions.get('permissions', []))
                    for perm in permissions:
                        print(f"Removing permission {perm['id']} for file {file.file.file_id} {instance.email}")
                        gdrive.unshare(perm['id'], file.file.file_id)




    elif action == "post_add":
        added_groups = Group.objects.filter(pk__in=pk_set)
        for group in added_groups:
            print(f'Group added: {group.name}')

            # Iterate over files that a group has access to
            gdrive_pages = GDrivePage.objects.filter(g_drive_groups__group=group)
            for gdrive_page in gdrive_pages:
                for file in gdrive_page.g_drive_page_files.all():
                    print(f'Sharing file {file.file.file_id} with {instance.email}')
                    gdrive.share_item(file.file.file_id, instance.email)




    elif action == "post_clear":
        print('All groups cleared')
        exit(1)
