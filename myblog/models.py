from django.db import models

# Create your models here.
class Blog(models.Model):


	class Meta:
		#для упорядочивания списка постов по дате публикации
		ordering = ['-date']

	title = models.SlugField(max_length=100, unique=True)
	text = models.TextField()
	date = models.DateTimeField('date published')
	#при использовании ImageField или FileField нужно настроить settings, media, в url указать debug=document_root=settings.MEDIA_ROOT И
	# в шаблонах указать ссылка изоброжения models.contextname.url и имя models.contextname.name
	image = models.ImageField(upload_to = 'image/', blank = True)#upload_to - путь сохранения файлов в media папку


	def __str__(self):
		return self.title

