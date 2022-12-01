from django.db import models
from django.urls import reverse


class Footballer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Article text")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Article created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Article updated at")
    published = models.BooleanField(default=True, verbose_name="Article published")
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name="Country")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article', kwargs={'article_slug': self.slug})
        return reverse('article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = 'Football player'
        verbose_name_plural = 'Football players'
        ordering = ['id']


class Country(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Country")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('country', kwargs={'country_slug': self.slug})
        return reverse('country', kwargs={'country_id': self.pk})

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['id']
