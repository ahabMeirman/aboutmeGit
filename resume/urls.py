from django.urls import path
from .views import *
from .view import * 

urlpatterns = [
	path('', skill_badges_group, name = 'my_resume_url'),
]