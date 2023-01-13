from django.db import models
from datetime import datetime

class Realtor(models.Model):
	name        = models.CharField(max_length = 25)
	photo       = models.ImageField(upload_to= 'photos/%Y/%m/%d')
	description = models.TextField()
	email       = models.EmailField()
	phone       = models.CharField(max_length = 10)
	top_seller  = models.BooleanField(default = False)
	date_hired  = models.DateTimeField(default = datetime.now)


	def __str__(self):
		return self.name
