import time
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	# past_26_year = time.localtime().tm_year - 20
	owner = models.ForeignKey('accounts.UserAccount',on_delete=models.CASCADE)
	first_name    = models.CharField(max_length = 10,blank=True)
	last_name     = models.CharField(max_length = 10,blank=True)
	# date_of_birth = models.DateTimeField()#default = dat)
	avatar  = models.ImageField(upload_to="uploads/profile")

	@property
	def get_profile_pic(self):
		return "http://localhost:8000" + self.avatar.url


	def __str__(self):
		return self.first_name