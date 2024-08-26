from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Folder, File
from .forms import FileUploadForm

def home(request):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(owner=request.user)
        return render(request, 'storage_app/home.html', {'folders': folders})
    else:
        return render(request, 'storage_app/home.html')

@login_required
def create_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        if folder_name:
            #This line creates a new Folder object in the database using Django's ORM (Object-Relational Mapping)
            folder = Folder.objects.create(name=folder_name, owner=request.user)
            return redirect('view_folder', folder_id=folder.id)
    return render(request, 'storage_app/create_folder.html')

@login_required
def view_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
    files = folder.files.all()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            folder.last_updated = timezone.now()  # Update the last updated timestamp
            folder.save()
            return redirect('view_folder', folder_id=folder.id)
    else:
        form = FileUploadForm()
    return render(request, 'storage_app/view_folder.html', {'folder': folder, 'files': files, 'form': form})

@login_required
def update_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
    if request.method == 'POST':
        new_name = request.POST.get('folder_name')
        if new_name:
            folder.name = new_name
            folder.last_updated = timezone.now()
            folder.save()
            return redirect('view_folder', folder_id=folder.id)
    return render(request, 'storage_app/update_folder.html', {'folder': folder})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    if file.folder.owner != request.user:
        return HttpResponseForbidden()
    file.delete()
    return redirect('view_folder', folder_id=file.folder.id)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  # Redirect to home page after logout
    return render(request, 'storage_app/logout.html')  # Render the logout confirmation page

class CustomLoginView(LoginView):
    template_name = 'storage_app/login.html'

login_view = CustomLoginView.as_view()
