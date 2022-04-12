import folium
map = folium.Map(location=[59.942012, 30.304139], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[59.942012, 30.304139], [59.93275224017821, 30.250921139378118], [59.92575930636877, 30.296494374976415]]:
    fg.add_child(folium.Marker(location=coordinates, popup="I am here", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
