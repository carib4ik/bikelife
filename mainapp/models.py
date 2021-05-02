from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Article(BaseModel):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='articles')
    file = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
