from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, related_name='hood_post')


    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    



class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    hood_image = CloudinaryField("image",null=True)
    description = models.TextField(max_length=600, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name        


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(null=True)
    neighbourhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Profile(models.Model):
  profile_pic = CloudinaryField("image")
  bio = models.TextField()
  contact=models.CharField(max_length=100)
  user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
  location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
  neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)

def save_profile(self):
    self.save()

def delete_profile(self):
     self.save()

def update_profile(self):
     self.save() 

@classmethod
def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

def _str_(self):
        return self.user.username


