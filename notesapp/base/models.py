from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='images',null=True,blank=True,default='/home/nidhin/Desktop/notesapp/notesapp/static/images/default.jpg')

    # USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Notes(models.Model):
    user=models.ForeignKey(CustomUser,null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(null=True,max_length=100)
    description=models.TextField(null=True)
    added=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

