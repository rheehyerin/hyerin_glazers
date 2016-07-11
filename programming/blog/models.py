from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to = 'mediafiles/uploaded/%Y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def lat(self):
        return self.lnglat.split(',')[1]

    def lng(self):
        return self.lnglat.split(',')[0]

