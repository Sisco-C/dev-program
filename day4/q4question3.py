# from geopy import location
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="locationfinder")
# enter the specified latitude and longitude
# Latitude = "1.2921"
# Longitude = "36.8219"
def get_details(coordinates):
# Location = geolocator.reverse(Latitude+ ","+Longitude)
    Location = geolocator.reverse(coordinates,exactly_one=True)
    address = Location.raw['address']
    #traverse the data
    city_name = address.get('city')
    state_name = address.get('state')
    country_name = address.get('country')
    return city_name, state_name, country_name
print(get_details("1.2921, 36.8219"))