from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    views = models.IntegerField(default=20)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return  self.title + ' by '+ self.author
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15] + "..." + " by " + self.user.username