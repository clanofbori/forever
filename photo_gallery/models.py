from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from ckeditor.fields import RichTextField


class Photo(models.Model):
    image = models.FileField(upload_to="/media/images/uploads/")
    title = models.CharField(max_length=255, null=True, blank=True)
    title_tag =models.CharField(max_length=255, blank=True)
    image_description = models.CharField(max_length=255, null=True, blank=True)
    meta_tag =models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)
    # add category field

    def get_absolute_url(self):
        return reverse('gallery')
