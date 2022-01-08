from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name = 'index'), 
    path('profile/', views.profile, name='profile'), 
    # path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('all_neighborhoods/',views.neighborhoods,name='hood'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood'),
    path('hood/<str:name>',views.lone_hood,name='lone_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path("create_business", views.create_business, name="create_business"),
    path("businesses/", views.businesses, name="businesses"),
    path('create_post', views.create_post, name='create_post'),
    path('posts/', views.posts, name = 'posts'),
    path('search/',views.search, name='search'),
    
]
