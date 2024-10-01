from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

photo_validator = FileExtensionValidator(['png', 'jpj', 'jpeg'])
file_validator = FileExtensionValidator(['txt', 'pdf', 'docx'])


def validate_file_minetype(file, accepted_list):
    file_mine_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mine_type not in accepted_list:
        raise ValidationError("Not supported file type")


def validate_image_minetype(file):
    accepted_list = ['image/png', 'image/jpeg', 'image/jpg']
    validate_file_minetype(file=file, accepted_list=accepted_list)


def validate_files_minetype(file):
    accepted_list = ['text/txt', 'application/pdf', 'text/docx']
    validate_file_minetype(file=file, accepted_list=accepted_list)



