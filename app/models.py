from django.db import models
from django.contrib.auth.models import User

# Create your models here.
     
# Create your models here.
class Likes(models.Model):
     Owner_ID=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
     like=models.IntegerField()
     # likes=models.ForeignKey(Blog,on_delete=models.CASCADE)
     
class Blog(Likes):
     Title = models.CharField(max_length=88)
     Content = models.TextField()
     is_public = models.BooleanField(default=False)

     
     def __str__(self):
          return self.Title