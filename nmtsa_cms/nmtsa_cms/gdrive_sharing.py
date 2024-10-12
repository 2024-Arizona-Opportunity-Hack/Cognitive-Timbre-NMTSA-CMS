from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import pprint

# Load the API key from the file
with open('nmtsa-cms-demo-cb62f7853dc0.json', 'r') as file:
    api_key_info = json.load(file)

def list_drive_files():
    # Authenticate and construct the service
    credentials = service_account.Credentials.from_service_account_info(api_key_info)
    service = build('drive', 'v3', credentials=credentials)
    
    # Call the Drive v3 API
    results = service.files().list(fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    
    if not items:
        print('No files found.')
    else:
        for item in items:
            print(f"{item['name']} ({item['id']})")


def share_drive_folder(folder_id, email, role='reader'):
    print(f"Sharing folder {folder_id} with {email} as {role}")

    # Authenticate and construct the service
    credentials = service_account.Credentials.from_service_account_info(api_key_info)
    service = build('drive', 'v3', credentials=credentials)

    
    
    # Create the permission
    permission = {
        'type': 'user',
        'role': role,
        'emailAddress': email
    }
    
    # Add the permission to the folder
    try:
        service.permissions().create(
            fileId=folder_id,
            body=permission,
            fields='id',
            sendNotificationEmail=False,
        ).execute()
        print(f"Permission granted to {email} for folder {folder_id}")
    except Exception as e:
        print(f"An error occurred: {e}")



def unshare(permission_id, file_id=None): 
    # Authenticate and construct the service
    credentials = service_account.Credentials.from_service_account_info(api_key_info)
    service = build('drive', 'v3', credentials=credentials)

    try:
        service.permissions().delete(
            fileId=permission_id if file_id is None else file_id,
            permissionId=permission_id,
        ).execute()
        print(f"Permission {permission_id} removed")
    except Exception as e:
        print(f"An error occurred: {e}")



# unshare('06448304225834008309', '16HulLskUaWMDMp5iOHgMnuL7s3JsatKY')


def list_perms():
    creds = service_account.Credentials.from_service_account_info(api_key_info)
    serv = build('drive', 'v3', credentials=creds)

    try:
        perms = serv.permissions().list(
            fileId='16HulLskUaWMDMp5iOHgMnuL7s3JsatKY',
            fields='permissions(id, role, type, emailAddress, displayName)',
            includePermissionsForView='published'
        ).execute()

        # Pretty print the permissions
        for perm in perms.get('permissions', []):
            perm_id = perm.get('id')
            role = perm.get('role')
            perm_type = perm.get('type')
            email_address = perm.get('emailAddress', 'N/A')
            display_name = perm.get('displayName', 'N/A')

            print(f"ID: {perm_id}, Role: {role}, Type: {perm_type}, Email: {email_address}, Display Name: {display_name}")

    except Exception as e:
        print(f"An error occurred: {e}")



# share_drive_folder('16HulLskUaWMDMp5iOHgMnuL7s3JsatKY', 'kchernov@asu.edu', 'writer')
list_perms()
# Example usage
# list_drive_files('nmtsa-cms-demo-cb62f7853dc0.json')