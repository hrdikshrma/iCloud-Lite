from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .forms import FileUploadForm
from .models import FileUpload
from .models import Profile
from django.shortcuts import get_object_or_404
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    files = FileUpload.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})


def delete_file(request, file_id):
    file_to_delete = get_object_or_404(FileUpload, id=file_id, user=request.user)
    if request.method == 'POST':
        file_to_delete.file.delete()  # This deletes the file from the filesystem
        file_to_delete.delete()       # This deletes the file record from the database
        return redirect('file_list')
    return render(request, 'confirm_delete.html', {'file': file_to_delete})
