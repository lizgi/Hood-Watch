from .models import Business, Location, Neighborhood, Post, Profile
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','contact') 


class HoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields = ['hood_image','name','description','occupants_count','location']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

    

