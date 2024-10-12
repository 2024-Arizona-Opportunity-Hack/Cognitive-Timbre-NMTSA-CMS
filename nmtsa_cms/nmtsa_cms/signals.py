import requests
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import Group, User
from django.dispatch import receiver
from django.core.signals import request_finished

test_dict = {
    
}

@receiver(m2m_changed, sender=User.groups.through)
def role_change_handler(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        print('Role change detected')
        user_groups = instance.groups.all()
        for group in user_groups:
            print(group.name)
        
        # # Make an external API call
        # api_url = "https://external-api.example.com/role-change"
        # payload = {
        #     "role_name": instance.name,
        #     "action": action
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer YOUR_API_TOKEN"
        # }
        
        # response = requests.post(api_url, json=payload, headers=headers)
        
        # if response.status_code == 200:
        #     print("API call successful")
        # else:
        #     print("API call failed")
