from geopy import location
from geopy.geocoders import Nominatim
geographiclocator = Nominatim(user_agent="geoapiExercises")
# enter the specified latitude and longitude
Latitude = "1.2921"
Longitude = "36.8219"
Location = geographiclocator.reverse(Latitude+ ","+Longitude)
address = location.raw['address']
city_name = address.get('city')
state_name = address.get('state')
country_name = address.get('country')
print('The city is : ' , city_name)
print('The state is : ', state_name)
print('The country is : ', country_name)
