from django.shortcuts import render
import folium 
import geocoder

# Create your views here.

def index(request):
    location = geocoder.osm('BR')
    lat = location.lat
    lng = location.lng
    country = location.country
    #Create Map Objet
    m = folium.Map(location=[19, -12], zoom_start=1.5)
    folium.Marker([-4.641122513190995, -40.56953464925870], tooltip='Clique aqui', popup='Nova Russas').add_to(m)
    folium.Marker([lat, lng], tooltip='Clique aqui', popup=country).add_to(m)
    #Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
            'm': m,
            }
    return render(request,'index.html',context)
