from django import forms

from .models import Feed

class FeedModelForm(forms.ModelForm):
	class Meta:
		model = Feed
		fields = [
			#"user",
			"description"
			


		]