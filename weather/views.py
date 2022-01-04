from django.shortcuts import render
from .models import City
import requests


# Create your views here.
def weather(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5660ed54eb409c5e35f94e0e82538ec5"
    cities=City.objects.all()
    weather_data=[]

    for city in cities:

        r=requests.get(url.format(city)).json()

        city_weather={
            'city': city.name,
            'temperature': int((int(r['main']['temp'])-32)*(5/9)) ,
            'description': (r['weather'][0]['description']).capitalize(),
            'icon':r['weather'][0]['icon'] ,
        }
        weather_data.append(city_weather)
    context={'city':weather_data}

    return render(request,'weather/weather.html',context)

def addcity(request):
    if request.method=='POST':
        if request.POST.get('name'):
            city=City()
            city.name=request.POST.get('name')
            city.save()
            return render(request,'weather/cities.html')
    else:
        return render(request,'weather/cities.html')

def deletecity(request):
    if request.method=='POST':
        if request.POST.get('name'):
            city_name=request.POST.get('name')
            city=City.objects.filter(name=city_name)
            city.delete()
            
            return render(request,'weather/cities.html')
    else:

        return render(request,'weather/cities.html')