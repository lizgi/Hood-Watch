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
        fields = ['hood_image','name','description','occupants_count','location','healthcenter_number','police_hotline']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content','location','neighborhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['name','image','email','description','location','neighborhood']                

