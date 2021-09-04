from django.urls import path
from .views import ( view_jobs, view_cached_jobs )
 
 
urlpatterns = [
    path('jobs/', view_jobs),
    path('cache/', view_cached_jobs),
  
]