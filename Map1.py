import folium
import pandas

data = pandas.read_csv("volcano.csv")
lat = list(data['Latitude'])
lon = list(data['Longitude'])
# volcano = list(data['V_Name'])
pei = list(data['PEI'])

def color_producer(pei_index):
    if pei_index < 2:
        return 'green'
    elif 2 <= pei_index < 4:
        return 'beige'
    elif 4 <= pei_index < 6:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[59.942012, 30.304139], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, pi in zip(lat, lon, pei):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,  popup=str(pi)+" PEI", fill_opacity=0.7,
                                     fill_color=color_producer(pi), color='grey', fill=True,
                                     icon=folium.Icon(color=color_producer(pi))))

map.add_child(fg)

map.save("Map1.html")
