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


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, verbose_name='Category', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})



class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Title', unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to= 'photo/%Y/%m/%d')
    high_price = models.FloatField()
    real_price = models.FloatField()
    views = models.IntegerField(default=0)
    bought = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})

