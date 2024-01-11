from django.core.exceptions import ValidationError
from .constants import VALID_IMAGE_EXTENSIONS, VALID_VIDEO_EXTENSIONS


def validate_video_or_image(value):
    valid_extensions = VALID_IMAGE_EXTENSIONS + VALID_VIDEO_EXTENSIONS

    file_name, file_extension = value.name.rsplit('.', 1)
    file_extension = '.' + file_extension.lower()

    if file_extension not in valid_extensions:
        raise ValidationError('Invalid file type. Only images (JPEG, PNG, GIF) and videos (MP4, MOV, AVI) are allowed.')
