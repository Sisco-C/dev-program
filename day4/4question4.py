from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
state = "Washington"
location = geolocator.geocode(state)
print('Country is: ' , location.address)