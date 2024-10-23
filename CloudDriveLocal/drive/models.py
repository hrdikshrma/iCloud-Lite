
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username


class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    

# class FileUpload(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='uploads/%Y/%m/%d/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.file.name

#     def get_file_url(self):
#         return default_storage.url(self.file.name)

#     def delete(self, *args, **kwargs):
#         # Delete the file from S3 when the model instance is deleted
#         self.file.delete(save=False)
#         super().delete(*args, **kwargs)

#     class Meta:
#         ordering = ['-uploaded_at']