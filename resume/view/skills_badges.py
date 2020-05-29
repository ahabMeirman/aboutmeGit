from resume.models import Skill
from django.shortcuts import render

def skill_badges_group(request):
	template_name = 'resume.html'
	skills = Skill.objects.all()
	context = {
		'skills' : skills
	}
	return render(request, template_name, context)