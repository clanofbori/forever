from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to="theblog/media/images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Photo(models.Model):
    image = models.FileField(upload_to="theblog/media/images/uploads/")
    title = models.CharField(max_length=255, null=True, blank=True)
    title_tag =models.CharField(max_length=255, blank=True)
    image_description = models.CharField(max_length=255, null=True, blank=True)
    meta_tag =models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('gallery')
