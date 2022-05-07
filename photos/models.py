from pyexpat import model
from unicodedata import category
from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True )
    name = models.CharField(max_length=100, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
      
        



class Memory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="pictures/")
    video = models.FileField(null=True, blank=True, upload_to="videos/")
    description = models.TextField()
    location = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = 'Memories'
        ordering = ['date']

       
    
    @property
    def videoURL(self):
        try:
           vid = self.video.url
        except:
           vid = ' '
        return vid

    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ' '
        return img




