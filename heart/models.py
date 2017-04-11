from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Htem(models.Model):
    values = models.DecimalField(max_digits=4, decimal_places=2)
    ctime = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return str(self.values)


class Hpres(models.Model):
    values = models.IntegerField()
    ctime = models.DateTimeField(default=timezone.now())


class Hrelax(models.Model):
    values = models.IntegerField()
    ctime = models.DateTimeField(default=timezone.now())


class Hpluse(models.Model):
    values = models.IntegerField()
    ctime = models.DateTimeField(default=timezone.now())
