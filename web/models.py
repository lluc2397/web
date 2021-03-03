from django.db import models
from datetime import date, datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from django_countries.fields import CountryField
from django.db.models import URLField
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog')

class PostWeb(models.Model):
    categoria = models.ForeignKey(Category, on_delete= models.PROTECT, blank=True, max_length= 200)
    title = models.CharField(max_length=300)
    slug = models.SlugField(null = True, blank=True)
    resumen = RichTextField()
    author= models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank=True, upload_to="media/")
    body = RichTextField()
    post_date = models.DateTimeField(default=timezone.now)
    likewp = models.ManyToManyField(MyUser, related_name='likes_wb', default = None, blank=True)

    def total_likes(self):
        return self.likewp.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
		    return reverse('home')

class CommentWeb(models.Model):
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(PostWeb, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ' | ' + str(self.post_connected.title)




