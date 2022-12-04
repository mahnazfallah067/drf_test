from django.db import models
from taggit.managers import  TaggableManager


# Create your models here.

class Book(models.Model):
    url = models.URLField()
    title = models.CharField(max_length= 120)
    content = models.TextField(max_length=200)
    summary = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images', default='', null=True, blank=True )
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=120)
    tags = TaggableManager()

    def __str__(self):
        return self.title + ' - ' + self.author
