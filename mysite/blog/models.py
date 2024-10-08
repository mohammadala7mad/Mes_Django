from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post (models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PU','Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    auther = models.ForeignKey(User , on_delete=models.CASCADE , related_name='blog_posts')
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2 , choices=Status.choices , default= Status.DRAFT)
     
    class Meta :
        ordering = ['-published']
        indexes = [
                      models.Index(fields=['-published']),
                  ]

    
    def __str__(self):
        return self.title
    