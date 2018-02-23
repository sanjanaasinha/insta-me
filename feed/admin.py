from django.contrib import admin

from .forms import FeedModelForm

from .models import Feed


class FeedModelAdmin(admin.ModelAdmin):
	#form_class = FeedModelForm
	class Meta:
		model = Feed


admin.site.register(Feed,FeedModelAdmin)
# Register your models here.
