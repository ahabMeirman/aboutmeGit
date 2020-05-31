from myblog.models import Blog
from django.shortcuts import render
from django.views.generic import View
from myblog.utils import * #все дополнит сокращения 

class Post(View):

	template_name = 'myblog/posts.html'

	def get(self, request):

		blogs = Blog.objects.all()

		context = {
			'blogs' : blogs
		}

		return render(request, self.template_name, context)

class ViewPostDetail(ObjectDaetailViewPostMixin, View):

	model = Blog
	template = 'myblog/post_detail.html'


