from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField()
    post_date=models.DateTimeField( default=timezone.now)
    post_update=models.DateTimeField( auto_now=True, auto_now_add=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
    

    class Meta:
        ordering=('-post_date',)



class Comment(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    comment_date=models.DateTimeField(  auto_now_add=True)
    body=models.TextField()
    active=models.BooleanField(default=False)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="comments")


    def __str__(self):
        return self.name