from django.db import models
from brands.models import Category
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)
    # ekta post multiple categorr moddhe thakte pre, abr eta category ar moddha multiple post thakte pre.
    author = models.ForeignKey(User,on_delete=models.CASCADE)    
    def __str__(self):
        return self.title
# set null o kra jte pre.....! 

