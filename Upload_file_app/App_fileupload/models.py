from django.db import models

def upload_path(instance, filename):
    return '/'.join(['uploadedfiles',str(instance.title), filename])

# Create your models here.
class file(models.Model):
    title=models.CharField(max_length=50, blank=False)
    uploadedfile=models.FileField(blank=True, null=True, upload_to=upload_path)