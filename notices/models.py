from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=80,unique=True)
    description = models.CharField(max_length=255,unique=True)