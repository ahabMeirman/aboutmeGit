from django.urls import path
from .views import *
from .view import * 

urlpatterns = [
	path('', Post.as_view(), name = 'post_url'), # список постов с пагинации 
	path('<str:title>/', ViewPostDetail.as_view(), name = 'post_detail_url'),
]