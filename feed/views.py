from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList
from django.db.models import Q
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy 
from django.views.generic  import  DeleteView, DetailView,ListView, CreateView, UpdateView
from .forms import FeedModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .mixins import FormUserNeededMixin,UserOwnerMixin
from .models import Feed

"""def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404 
		
	form = FeedModelForm(request.Feed or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "form.html", context)


	def post_detail(request, slug=None):
		instance = get_object_or_404(Post, slug=slug)
		if instance.publish > timezone.now().date() or instance.draft:
			if not request.user.is_staff or not request.user.is_superuser:
				raise Http404
				share_string = quote_plus(instance.description)
				context = {
				"description": instance.description,
				"instance": instance,
				"share_string": share_string,
				}
				return render(request, "feed_detail.html", context)"""

	




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
	success_url = reverse_lazy("home")
	

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
		
		query = self.request.GET.get("q", None)
		if query is not None:
			qs=qs.filter(
				Q(description__icontains= query) |
				Q(user__username__icontains=query)
				)

		return qs


	def get_context_data(self, *args,**kwargs):
		context = super(FeedListView, self).get_context_data(*args,**kwargs)
		context['create_form'] = FeedModelForm
		context['create_url'] = reverse_lazy ('feed:create')
		return context

	def feed_detail_view(request, pk= None):
		obj=get_object_or_404(Feed,pk=pk)
		print(obj)
		context = {
			"object": obj
		}
		return render(request,"feed/detail_view.html", context)


# Create your views here."""
