from django.db import models

class 	Feed(models.Model):
	document =	models.FileField(upload_to='static/documents/', blank=False, null=False)
	description	=	models.CharField(max_length=255,blank=False)

	def __str__(Self):
		return str(Self.description)
		
	


# Create your models here.


