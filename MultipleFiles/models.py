# from django.db import models

# Create your models here.
# class MyFileUpload(models.Model):    
#     my_file=models.FileField()

# from django.db import models
 
# Create your models here.
 
# class FileList(models.Model):
#     # file_path = models.FileField(blank=True,null = True, upload_to='fileuploads/')
#     title = models.CharField(max_length=255, blank=True)
#     file = models.FileField(upload_to='fileuploads/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)