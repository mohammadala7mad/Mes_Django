from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('',view=views.all_posts , name='all_posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',view=views.post_detail , name='post_detail'),
]
