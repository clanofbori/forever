from django import forms
from .models import Post, Categories, Photo

choices = Categories.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet',
                  'header_image', 'image_description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'',
                                             'id':'user_id_tag', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'image_description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ('title', 'title_tag', 'author', 'body', 'snippet',
                  'header_image', 'image_description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'image_description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)

        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
