from django.db import models

# Create your models here.

class ShortURL(models.Model):
    original_url = models.URLField()
