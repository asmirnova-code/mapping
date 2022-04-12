import folium
import pandas

data = pandas.read_csv("volcano.csv")
lat = list(data['Latitude'])
lon = list(data['Longitude'])

map = folium.Map(location=[59.942012, 30.304139], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="I am here", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
