from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import pprint
__MAIN_FOLDER_NAME = '16HulLskUaWMDMp5iOHgMnuL7s3JsatKY'


# Load the API key from the file
with open('nmtsa-cms-demo-cb62f7853dc0.json', 'r') as file:
    api_key_info = json.load(file)


def folder_folders(folder_id=__MAIN_FOLDER_NAME):
    # Authenticate and construct the service
    credentials = service_account.Credentials.from_service_account_info(api_key_info)
    service = build('drive', 'v3', credentials=credentials)
    
    # Query to get all folders within the given folder_id
    query = f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'"
    results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
    folders = results.get('files')
    
    pprint.pprint(folders)

    return folders

def folder_files(folder_id=__MAIN_FOLDER_NAME):
    # Authenticate and construct the service
    credentials = service_account.Credentials.from_service_account_info(api_key_info)
    service = build('drive', 'v3', credentials=credentials)
    
    # Query to get all mp4 files within the given folder_id
    query = f"'{folder_id}' in parents and mimeType = 'video/mp4'"
    results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
    files = results.get('files')
    
    pprint.pprint(files)

    return files

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


def share_item(item_id, email, role='reader'):
    print(f"Sharing folder {item_id} with {email} as {role}")

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
            fileId=item_id,
            body=permission,
            fields='id',
            sendNotificationEmail=False,
        ).execute()
        print(f"Permission granted to {email} for folder {item_id}")
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


def list_perms(file_id):
    creds = service_account.Credentials.from_service_account_info(api_key_info)
    serv = build('drive', 'v3', credentials=creds)

    
    return serv.permissions().list(
        fileId=file_id,
        fields='permissions(id, emailAddress)',
        includePermissionsForView='published'
    ).execute()




# share_drive_folder('1mXbY3yFf66EIYSKhq7sjSylUDyCH-4KF', 'tupreti@asu.edu', 'writer')
# list_perms()
# Example usage
# list_drive_files('nmtsa-cms-demo-cb62f7853dc0.json')
folder_folders()
print('----------------------------------')
folder_files()
print('----------------------------------')