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

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, pi in zip(lat, lon, pei):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6,  popup=str(pi)+" PEI", fill_opacity=0.7,
                                     fill_color=color_producer(pi), color='grey', fill=True,
                                     icon=folium.Icon(color=color_producer(pi))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
