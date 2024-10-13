import requests
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import Group, User
from django.dispatch import receiver
from django.core.signals import request_finished

test_dict = {
    
}

@receiver(m2m_changed, sender=User.groups.through)
def role_change_handler(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        added_groups = Group.objects.filter(pk__in=pk_set)
        for group in added_groups:
            print(f'Group added: {group.name}')
            # Handle added groups here
            # Example: Make an external API call for added groups
            # api_url = "https://external-api.example.com/role-change"
            # payload = {
            #     "role_name": group.name,
            #     "action": "added"
            # }
            # headers = {
            #     "Content-Type": "application/json",
            #     "Authorization": "Bearer YOUR_API_TOKEN"
            # }
            # response = requests.post(api_url, json=payload, headers=headers)
            # if response.status_code == 200:
            #     print("API call successful for added group")
            # else:
            #     print("API call failed for added group")

    elif action == "post_remove":
        removed_groups = Group.objects.filter(pk__in=pk_set)
        for group in removed_groups:
            print(f'Group removed: {group.name}')
            # Handle removed groups here
            # Example: Make an external API call for removed groups
            # api_url = "https://external-api.example.com/role-change"
            # payload = {
            #     "role_name": group.name,
            #     "action": "removed"
            # }
            # headers = {
            #     "Content-Type": "application/json",
            #     "Authorization": "Bearer YOUR_API_TOKEN"
            # }
            # response = requests.post(api_url, json=payload, headers=headers)
            # if response.status_code == 200:
            #     print("API call successful for removed group")
            # else:
            #     print("API call failed for removed group")

    elif action == "post_clear":
        print('All groups cleared')
        # Handle clearing of all groups here
        # Example: Make an external API call for clearing all groups
        # api_url = "https://external-api.example.com/role-change"
        # payload = {
        #     "role_name": "all",
        #     "action": "cleared"
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer YOUR_API_TOKEN"
        # }
        # response = requests.post(api_url, json=payload, headers=headers)
        # if response.status_code == 200:
        #     print("API call successful for clearing all groups")
        # else:
        #     print("API call failed for clearing all groups")
