
from django.conf.urls import url
from django.views.generic.base import RedirectView


from .views import (
	FeedDetailView,
	FeedDeleteView,
	FeedListView,
	FeedCreateView,
	FeedUpdateView,
	)

urlpatterns = [
    url(r'^$',RedirectView.as_view(url="/")),
	url(r'^search$',FeedListView.as_view(), name='home'),
	url(r'^create/$',FeedCreateView.as_view(), name='create'),    
    url(r'^(?P<pk>\d+)/update/$',FeedUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$',FeedDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$',FeedDeleteView.as_view(), name='delete')
]

 