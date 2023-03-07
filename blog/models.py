from django.db import models

class Topic(models.Model):
	"""Topic being documented"""
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	intro = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""string rep of the model"""
		return self.title


class Content(models.Model):
	"""Topic content"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	author_name = models.CharField(max_length=200, blank=False, null=True)
	author_image = models.ImageField(upload_to='uploads', blank=False, null=True)
	highlights = models.TextField(blank=True)
	text = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""string rep of the model"""
		return self.author_name


class Comment(models.Model):
	"""comments"""
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	username = models.CharField(max_length=200, blank=False, null=True)
	text = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""string rep of the model"""
		return self.username
