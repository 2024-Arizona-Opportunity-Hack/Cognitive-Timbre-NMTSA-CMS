from django.shortcuts import render
from wagtail.admin import widgets

from nmtsa_cms.gdrive_sharing import folder_files
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def manage_files_view(request):
    # Render a simple page for file management
    list_of_files = folder_files()
    return render(request, 'manage_files.html', {'files': list_of_files})

@csrf_protect
def manage_files_submit(request):
    if request.method == 'POST':
        selected_files = request.POST.getlist('file_checkbox')
        print('Selected files:', selected_files)
        # Process the selected files as needed
        list_of_files = folder_files()
        return render(request, 'manage_files.html', {'files': list_of_files, 'selected_files': selected_files})
    else:
        return HttpResponse(status=405)  # Method Not Allowed
