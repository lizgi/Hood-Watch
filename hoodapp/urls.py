from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name = 'index'), 
    path('profile/', views.profile, name='profile'), 
    path('create_profile/',views.create_profile,name = 'create_profile'),
]
