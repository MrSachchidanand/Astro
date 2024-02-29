import geocoder
import folium

g  = geocoder.ip("13.127.186.134")
sui = g.latlng
miu = geocoder.location(sui)

mapu = folium.Map(location=sui,
                  zoom_start=12)
folium.Marker(location=sui).add_to(mapu)

print(miu)
