from rest_framework import generics
from feed.models import Feed
from django.db.models import Q
from rest_framework import permissions
from .serializers import FeedModelSerializer

class FeedCreateAPIView(generics.CreateAPIView):
	serializer_class= FeedModelSerializer
	permission_classes=[permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user =self.request.user)



class FeedListAPIView(generics.ListAPIView):
	serializer_class= FeedModelSerializer

	def get_queryset(self, *args, **kwargs):
		qs=Feed.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs=qs.filter(
				Q(description__icontains = query) |
				Q(user__username__icontains = query)
				)

		return qs