from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

photo_validator = FileExtensionValidator(['png', 'jpg', 'jpeg'])
file_validator = FileExtensionValidator(['txt', 'pdf', 'doc', 'docx'])


def validate_file_mimetype(file, accepted_list):
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in accepted_list:
        raise ValidationError("Not supported file type")


def validate_image_mimetype(file):
    accepted_list = ['image/png', 'image/jpeg', 'image/jpg']
    validate_file_mimetype(file=file, accepted_list=accepted_list)


def validate_specs_mimetype(file):
    accepted_list = ['text/plain', 'application/pdf', 'application/msword',
                     'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    validate_file_mimetype(file=file, accepted_list=accepted_list)



