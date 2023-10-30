from django import forms
from .models import Photo
from .validators import validate_video_or_image
from .constants import VALID_IMAGE_EXTENSIONS, VALID_VIDEO_EXTENSIONS


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)

        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        validate_video_or_image(image)

        return image
