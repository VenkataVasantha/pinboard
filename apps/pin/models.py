from django.db import models

class Board(models.Model):

    title     = models.CharField(max_length=100)
    blurb     = models.CharField(max_length=100)
    author    = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    details   = models.CharField(max_length=100)

