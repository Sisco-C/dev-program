from geopy.geocoders import Nominatim
# initializing Nominatip API using geoapiExercises parameter
geolocator = Nominatim(user_agent="geoapiExercises")
#getting comlete adress using geocode()
place = input ("Enter zip code:")
location = geolocator.geocode(place)
print(location.address)