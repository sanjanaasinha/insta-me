from django import forms

from .models import Feed

class FeedModelForm(forms.ModelForm):
	image= forms.FileField()
	description= forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "describe", "class": "form-control"}))
	class Meta:
		model = Feed
		fields = [
			#"user",
			"image",
			"description"
			
			


		]