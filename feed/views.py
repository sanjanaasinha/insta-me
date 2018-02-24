from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList
from django.db.models import Q
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy 
from django.views.generic  import  DeleteView, DetailView,ListView, CreateView, UpdateView
from .forms import FeedModelForm
from .mixins import FormUserNeededMixin,UserOwnerMixin
from .models import Feed


class FeedCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
	form_class = FeedModelForm
	template_name = "feed/create_view.html"
	# success_url = "/feed/create/"
	login_url = "/admin/"

class FeedUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
	queryset = Feed.objects.all()
	form_class = FeedModelForm
	template_name = "feed/update_view.html"
	

class FeedDeleteView(LoginRequiredMixin,DeleteView):
	model = Feed
	template_name = "feed/confirm_delete.html"
	success_url = reverse_lazy("feed:list")
	#= reverse_lazy("feed:list")


class FeedDetailView(DetailView):
	#template_name="feed/detail_view.html" 
	queryset = Feed.objects.all()

	#def get_object(self):
		# pk = self.kwargs.get("pk")
		#print(pk)
		#return Feed.objects.get(pk =pk)

class FeedListView(ListView):
	#queryset = Feed.objects.all()
	def get_queryset(self, *args, **kwargs):
		qs=Feed.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs=qs.filter(
				Q(description__icontains= query) |
				Q(user__username__icontains=query)
				)

		return qs


	def get_context_data(self, *args,**kwargs):
		context = super(FeedListView, self).get_context_data(*args,**kwargs)
		#print(context)
		return context

	def feed_detail_view(request, pk= None):
		obj=get_object_or_404(Feed,pk=pk)
		print(obj)
		context = {
			"object": obj
		}
		return render(request,"feed/detail_view.html", context)


# Create your views here."""
