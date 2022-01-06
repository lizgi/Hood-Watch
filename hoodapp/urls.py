from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name = 'index'), 
    path('profile/', views.profile, name='profile'), 
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('all_neighborhoods/',views.neighborhoods,name='hood'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood'),
    path('hood/<str:name>',views.lone_hood,name='lone_hood'),
    path('join_hood/<id>', views.join_neighborhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighborhood, name='leave-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
]
