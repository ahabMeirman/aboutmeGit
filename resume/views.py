from django.shortcuts import render, redirect


# Create your views here.

def my_resume(request):
	return render(request, 'resume.html')