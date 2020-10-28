from django.db import models

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400 , null = True , blank = True)
    creat_at = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(max_length=100,blank=True , null=True)


    def __ste__(self):
        return self.title


