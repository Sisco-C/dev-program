from geopy.geocoders import Nominatim
# initializing Nominatip API using geoapiExercises parameter
locator = Nominatim(user_agent="geoapiExercises")
#getting comlete adress using geocode()
location = input ("Enter zip code:")
location = locator.geocode()
data = location.raw
location_data = data['display_name']. split()
print(location_data)