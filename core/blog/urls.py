from django.urls import path
from .views import CarsViewset

app_name = 'blog'

urlpatterns= [
    path('cars/', CarsViewset.as_view()),
    path('cars/<int:id>', CarsViewset.as_view()),
    
   
]