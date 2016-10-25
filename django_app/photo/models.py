from django.db import models
from django.conf import settings



class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=80)


class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True)
    img = models.ImageField(uplaoad_to='photo')
