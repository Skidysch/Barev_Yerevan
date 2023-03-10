from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(unique=True, max_length=100, verbose_name='Slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=200,
        verbose_name='Slug'
    )
    categories = models.ManyToManyField(Category, verbose_name='Category')
    description = models.TextField(blank=True, verbose_name='Description')
    address = models.CharField(max_length=200, verbose_name='Address')
    photo = models.ImageField(
        upload_to='sightseeing_photos/%Y/%m/%d/',
        verbose_name='Photo'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation time'
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Update time'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Is published?'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place', kwargs={'place_slug': self.slug})

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        ordering = ['id']


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sightseeing = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sightseeing.name}"
