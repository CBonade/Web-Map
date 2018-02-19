import folium
import pandas as pd

data = pd.read_csv('Volcanoes_USA.txt', sep=',')

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_picker(el):
    if el <= 2000:
        return "green"
    elif el <= 3000:
        return "orange"
    elif el > 3000:
        return "red"


map = folium.Map(location=[32.554114, -90.386122],
                 zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], radius=7, fill=True, color="grey", fill_color=color_picker(el), fill_opacity=1,
        popup=folium.Popup("Elevation: " + str(el) + " m", parse_html=True)))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
