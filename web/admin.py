from django.contrib import admin
from .models import PostWeb, CommentWeb, Category

admin.site.register(PostWeb)
admin.site.register(CommentWeb)
admin.site.register(Category)