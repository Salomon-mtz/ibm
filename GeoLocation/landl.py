from geopy.geocoders import Nominatim
import gmplot

casilla = input("Inserte la colonia: ")
geolocator = Nominatim(user_agent="Name")
location = geolocator.geocode(casilla)

gmap = gmplot.GoogleMapPlotter(location.latitude, location.longitude, 18)


gmap.apikey = "AIzaSyBoxtOSE3UPpsHJSJx8KaaeotdsfgwHoCc"
gmap.draw( "C:\\Users\\USER\\Desktop\\colonia.html" )
