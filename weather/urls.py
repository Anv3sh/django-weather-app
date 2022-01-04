from django.urls import include, path
from .models import City
from .views import weather,addcity,deletecity

urlpatterns = [
   path('',weather,name='weather-app'),
   path('add-city',addcity,name= 'add-city'),
   path('delete-city',deletecity, name='delete-city')
]