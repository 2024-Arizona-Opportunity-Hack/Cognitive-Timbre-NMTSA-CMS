import requests
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import Group, User
from django.dispatch import receiver
from django.core.signals import request_finished

from nmtsa_cms.gdrive_sharing import *
import pprint

test_dict = {
    'Moderators': [],
    'Editors': [],
    'admin': [],
}

@receiver(m2m_changed, sender=User.groups.through)
def role_change_handler(sender, instance, action, pk_set, **kwargs):
    if action == "post_remove":
        removed_groups = Group.objects.filter(pk__in=pk_set)

        # Iterate over removed groups, 
        for group in removed_groups:
            print(f'Group removed: {group.name}')

            # Iterate over files that a group has access to
            for file in test_dict.get(group.name, []):
                
                # Get permissions for the file
                permissions = list_perms(file)

                # pprint.pprint(permissions)

                permissions = filter(lambda x: x.get('emailAddress') == instance.email, permissions.get('permissions', []))
                for perm in permissions:
                    print(f"Removing permission {perm['id']} for file {file} {instance.email}")
                    unshare(perm['id'], file)



    
    elif action == "post_add":
        added_groups = Group.objects.filter(pk__in=pk_set)
        for group in added_groups:
            print(f'Group added: {group.name}')

            # Iterate over files that a group has access to
            for item in test_dict.get(group.name, []):
                
                share_item(item, instance.email)
            



    elif action == "post_clear":
        print('All groups cleared')
        exit(1)
