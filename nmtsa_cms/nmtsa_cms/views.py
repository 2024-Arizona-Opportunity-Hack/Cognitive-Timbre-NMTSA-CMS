from django.shortcuts import render
from wagtail.admin import widgets

from nmtsa_cms.gdrive_sharing import folder_files

def manage_files_view(request):
    # Render a simple page for file management
    list_of_files = folder_files()
    return render(request, 'manage_files.html', {'files': list_of_files})
