from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

class Meta(models.Model):
    site_title = models.CharField(max_length=65,default="")
    navbar_title = models.CharField(max_length=65,default="")
    footer_left = models.TextField(default="")
    column_left_color = models.CharField(max_length=65,default="")
    column_mid_color = models.CharField(max_length=65,default="")
    column_right_color = models.CharField(max_length=65,default="")
   