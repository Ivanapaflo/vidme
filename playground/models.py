from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    video_file=models.FileField(upload_to='uploads/video_files', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail=models.FileField(upload_to='uploads/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    date_published=models.DateTimeField(default=timezone.now)
    Description=models.TextField(default=timezone.now)
    ratings= models.FloatField()

    def __str__(self):
       return self.title
