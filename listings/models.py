from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from realtors.models import Realtor


class Listing(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE   = 'For Sale'
        FOR_RENT   = 'For rent'


    class HomeType(models.TextChoices):
        APARTAMA  = 'Apartama'
        CONDO     = 'Condo'
        TOWNHOUSE = 'Townhouse'


    realtor       = models.ForeignKey(Realtor, related_name='realtors', on_delete=models.CASCADE)
    title         = models.CharField(max_length=255)
    slug          = models.SlugField()
    address       = models.CharField(max_length=255)
    city          = models.CharField(max_length=255)
    state         = models.CharField(max_length=255)
    house_number  = models.CharField(max_length=255)
    price         = models.DecimalField(max_digits=6, decimal_places=2,default=144)
    published     = models.BooleanField(default = False)
    sale_type     = models.CharField(max_length = 10,choices = SaleType.choices,default = SaleType.FOR_SALE)
    bed_rooms     = models.IntegerField()
    bath_rooms    = models.IntegerField(default = 0)
    sqrt          = models.DecimalField(max_digits = 4,decimal_places = 2)
    home_type     = models.CharField(max_length = 10,choices = HomeType.choices,default = HomeType.CONDO)
    description   = models.TextField(blank=True, null=True)
    avgRating     = models.IntegerField(default=1)
    ratings       = models.IntegerField(default=1)
    oldPrice      = models.DecimalField(max_digits=6, decimal_places=2,default=144)
    image         = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    image_1       = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    image_2       = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    image_3       = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    image_4       = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    image_5       = models.ImageField(upload_to='uploads/', default = None, blank=True, null=True)
    date_added    = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Listings"
        ordering = ('-date_added',)
    objects   = models.Manager()








    def __str__(self):
        return self.title

    @property
    def images(self):

        return [
            'http://10.0.3.2:8000' + self.image_1.url if self.image_1.url else 'http://10.0.3.2:8000' + self.image.url,
            'http://10.0.3.2:8000' + self.image_1.url if self.image_1.url else 'http://10.0.3.2:8000' + self.image.url,
            'http://10.0.3.2:8000' + self.image_2.url if self.image_2.url else 'http://10.0.3.2:8000' + self.image.url,
            # 'http://10.0.3.2:8000' + self.image_3.url if self.image_3.url else 'http://10.0.3.2:8000' + self.image.url,


            ]

    
    def get_absolute_url(self):
        return f'/api/v1/listings/{self.slug}/'
    
    @property
    def get_image(self):
        if self.image:
            return 'http://10.0.3.2:8000' + self.image.url + '/'
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


