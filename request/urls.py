from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # Home page (customer view)
    path('submit/', views.submit_request, name='submit_request'),  # Form submission page
   
]
