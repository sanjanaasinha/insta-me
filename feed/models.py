from django.conf import settings
from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError

def validate_description(value):
	description = value
	if description == "bjp":
		raise ValidationError("cannot be anything about bjp")
	return value

class 	Feed(models.Model):
	user =	models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	
	description	=	models.CharField(max_length=255,blank=False, validators=[validate_description])
	updated =	models.DateTimeField(auto_now=True)

	def __str__(Self):
		return str(Self.description)
		
	def get_absolute_url(self):
		return reverse("feed:detail", kwargs ={"pk":self.pk})
	


# Create your models here.


