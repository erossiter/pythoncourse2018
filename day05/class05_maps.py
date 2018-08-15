#### Class05
#### Googlemaps API

# pip install googlemaps
## https://console.developers.google.com/apis/credentials?project=_
## need geocoding and distance matrix APIs enabled
import imp
imported_items = imp.load_source('pythoncourse2018', '../../pythoncourse2018-prep/day05/erinkeys/googlekeys.py')

gmaps = imported_items.gmaps

whitehouse = 'The White House'
location = gmaps.geocode(whitehouse)
location ## again, sooo much data 
location[0].keys()

location[0]['geometry'].keys()

location[0]['geometry']['location']

latlong = location[0]['geometry']['location']

destination = gmaps.reverse_geocode(latlong)
## sometimes you have to dig...
print destination[0]["address_components"][0]["short_name"] 


duke = gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke = duke[0]['geometry']['location']

washu = gmaps.geocode('1 Brookings Dr, St. Louis, MO 63130')
washu = washu[0]['geometry']['location']

distance = gmaps.distance_matrix(duke, latlong)
print distance['rows'][0]['elements'][0]['distance']['text']



## Plotting --------------------------------------------------------------
## https://github.com/vgm64/gmplot
#pip install gmplot
from gmplot import gmplot

## location and zoom level
## can use latitutde and longitude instead
plot1 = gmplot.GoogleMapPlotter.from_geocode("St. Louis", 13)



stl_places = ["Forest Park, St. Louis",
"Missouri Botanical Garden, St. Louis",
"Anheuser Busch, St. Louis",
"Arch, St. Louis"]

def grab_latlng(place):
	x = gmaps.geocode(place)
	return (x[0]["geometry"]["location"]["lat"], x[0]["geometry"]["location"]["lng"])

l = [grab_latlng(i) for i in stl_places]

attraction_lats, attraction_lons = zip(*l)

plot1.scatter(attraction_lats, attraction_lons,
	'black',
	size=40,
	marker=True)

# Draw
plot1.draw("my_map.html")





# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? You will get errors - debug
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]