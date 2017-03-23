from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bbs(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField(default=0)
    ranking = models.IntegerField()
    Created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    adminstrator = models.ForeignKey('BBS_user')


class BBS_user(models.Model):
    user = models.OneToOneField(User)
    # django user management system
    signature = models.CharField(max_length=128, default='no signature')
    photo = models.ImageField(upload_to="upload_imgs/",
            default="upload_imgs/user.jpg")

    def __unicode__(self):
        return self.user.username
