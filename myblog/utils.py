from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Blog

class ObjectDaetailViewPostMixin:

	model = None
	template = None

	def get(self, request, *args, **kwargs):

		obj = get_object_or_404(self.model, title__iexact = self.kwargs["title"])

		context = {
			self.model.__name__.lower() : obj,

		}
		return render(request, self.template, context)