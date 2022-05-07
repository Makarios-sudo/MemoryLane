from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank =True, null= True, upload_to="profile/", default = 'profile/defaultP.jpeg')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.username)

    @property
    def imageURL(self):
        try:
            img = self.image.url
        except:
            img = ' '
        return img




