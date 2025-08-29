from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	email = models.EmailField(unique=True)

class Review(models.Model):
	Movie_title=models.CharField(max_length =250)
	Review_Content = models.TextField(max_length = 250)
	Rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])	
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	Created_date = models.DateField(auto_now_add=True)