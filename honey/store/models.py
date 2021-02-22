from django.db import models
from django.urls import reverse


# Create your models here.

class PostTag(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=65, verbose_name='slug', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    first_photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='main photo')
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(PostTag, related_name='posts')
    as_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
