from django.urls import path
from . import views

urlpatterns = [ 
    path('track/', views.track_request, name='track_request'), 
    path('', views.home, name='home'), 
    path('submit/', views.submit_request, name='submit_request'), 
    path('request/submit/', views.submit_request, name='submit_request'),
]
