from django.db import models
from .validators import photo_validator, file_validator, validate_file_minetype, validate_files_minetype, validate_image_minetype


class MyMedia(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files', validators=[photo_validator, validate_files_minetype])
    image = models.ImageField(upload_to='images', validators=[file_validator, validate_image_minetype])

    def __str__(self):
        return self.title

