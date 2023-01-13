from io import BytesIO
from PIL import Image
from django.contrib.auth.models import User

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural="Categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class HouseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = True)
     

class House(models.Model):
    category      = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title         = models.CharField(max_length=255)
    is_published  = models.BooleanField(default = False)
    slug          = models.SlugField()
    description   = models.TextField(blank=True, null=True)
    avgRating     = models.IntegerField(default=1)
    price         = models.DecimalField(max_digits=6, decimal_places=2,default=144)
    oldPrice      = models.DecimalField(max_digits=6, decimal_places=2,default=144)
    image         = models.ImageField(upload_to='uploads/', blank=True, null=False)
    image_1       = models.ImageField(upload_to='uploads/', blank=True, null=False)
    image_2       = models.ImageField(upload_to='uploads/', blank=True, null=False)
    image_3       = models.ImageField(upload_to='uploads/', blank=True, null=False)
    image_4       = models.ImageField(upload_to='uploads/', blank=True, null=False)
    image_5       = models.ImageField(upload_to='uploads/', blank=True, null=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('accounts.UserAccount', related_name='houses', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Houses"
        ordering = ('-date_added',)
    objects   = models.Manager()
    published = HouseManager()


    def __str__(self):
        return self.title

    @property
    def images(self):
        return [
                'http://127.0.0.1:8000' + self.image_1.url if self.image_1.url else 'http://127.0.0.1:8000' + self.image.url,
                'http://127.0.0.1:8000' + self.image_2.url if self.image_1.url else 'http://127.0.0.1:8000' + self.image.url,
                'http://127.0.0.1:8000' + self.image_3.url if self.image_3.url else 'http://127.0.0.1:8000' + self.image.url,
                'http://127.0.0.1:8000' + self.image_4.url if self.image_4.url else 'http://127.0.0.1:8000' + self.image.url,
               'http://127.0.0.1:8000' + self.image_5.url if self.image_5.url else 'http://127.0.0.1:8000' + self.image.url,
                ]
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def hero_count(self,):
        return self.hero_set.count()

        
    def villain_count(self):
        return self.villain_set.count()

