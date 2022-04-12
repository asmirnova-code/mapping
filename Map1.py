import folium
map = folium.Map(location=[59.942012, 30.304139], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[59.942012, 30.304139], popup="I am here", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
