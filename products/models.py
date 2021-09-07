from django.db import models

# Create your models here.
class Product(models.Model):
	title  = models.CharField(max_length = 120)
	description = models.TextField(null =True , blank =  True) # su mo ta
	price = models.DecimalField(decimal_places = 2 , max_digits =100 ) # gia ban
	summary = models.TextField(null =False , blank =True) # tom luoc
	featured = models.BooleanField(default =False)#null =true , default =true
