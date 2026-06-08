from django.db import models
import random
import string
from django.contrib.auth.models import User

# Create your models here.
def short_key_generation():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_key = models.CharField(max_length=20, unique=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    
    def save(self, *args, **kwargs):
        if not self.short_key:
            key = short_key_generation()
            while ShortURL.objects.filter(short_key=key).exists():
                key = short_key_generation()
            self.short_key = key
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_key} → {self.original_url}"
