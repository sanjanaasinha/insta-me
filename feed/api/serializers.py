from rest_framework import serializers
from feed.models import Feed
from accounts.api.serializers import UserDisplaySerializer



class FeedModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only= True)
	class Meta:
		model = Feed
		fields = [
			'user',
			'description',
			'image'


		]
