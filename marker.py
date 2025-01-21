#aqui eu consigo adicionar ao popup do marcador a conversão automatica de coordenadas geograficas
#para utm

import folium
import utm

def convert_to_utm(latitude, longitude):
    utm_coords = utm.from_latlon(latitude, longitude)
    return utm_coords[0], utm_coords[1]

#Coordenadas geográficas de exemplo
latitude = -28.12694443
longitude = -49.47972221

#Convertendo para UTM
utm_easting, utm_northing = convert_to_utm(latitude, longitude)

#Criar um mapa
m = folium.Map(location=[latitude, longitude], zoom_start=13)

#Adicionar marcador com informações de coordenadas
folium.Marker(
    location=[latitude, longitude],
    popup=f'Geográficas: Lat {latitude}, Lon {longitude}<br>UTM: Easting {utm_easting}, Northing {utm_northing}'
).add_to(m)

# Salvar o mapa como um arquivo HTML
m.save("mapa_interativo.html")

# Instrução para indicar que o mapa foi salvo
print("Mapa salvo como mapa_interativo.html")


#comando para rodar o código no terminal
#python marker.py

#comando para abrir no navegador pelo terminal
#start mapa_interativo.html
