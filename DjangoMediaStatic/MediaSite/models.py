from django.db import models
from .validators import photo_validator, file_validator, validate_specs_mimetype, validate_image_mimetype


class MyMedia(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files', validators=[file_validator, validate_specs_mimetype])
    image = models.ImageField(upload_to='images', validators=[photo_validator, validate_image_mimetype])

    def __str__(self):
        return self.title

