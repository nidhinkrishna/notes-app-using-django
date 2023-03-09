from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='profile',null=True,blank=True)

    # USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]