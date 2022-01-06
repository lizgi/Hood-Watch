from django.contrib import admin
from .models import Business, Location, Neighborhood, Post, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)