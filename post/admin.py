from django.contrib import admin
from .models import Post

# Register your models here.

class AdminPost(admin.ModelAdmin):

    model = Post
    list_display = ['title' ,'creat_at' ]


admin.site.register(Post, AdminPost)