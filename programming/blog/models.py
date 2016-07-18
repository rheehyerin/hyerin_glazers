from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to = 'media/uploaded/%Y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_content(self):
        return self.content


class Portfolio_content(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='media/uploaded/%Y')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    def delete(self, *args, **kwargs):
        self.video.delete()
        super(Portfolio_content, self).delete(*args, **kwargs)
