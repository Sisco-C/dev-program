from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('DEVICE LOCATION-FINDER APP '))

import socket
import requests
import json

google_map_api_key = "AIzaSyAS-soEXp_eCcyQ9JrT-qDOBapj-l5m2to"
ip_stack_api_key = "077d18d9cb8e8dd7ef1b299d2f0410c5"

ip_address = input("Enter your device's IP Address:") or "ip_addresses"

# Get host name
def get_host_ip():

    ip_addresses = socket.gethostbyname_ex(socket.gethostname())
   
    res = ip_addresses[2]
    return_type = type(res)
    return ip_addresses[2][0]
        

def get_coordinates(ip_address):
    res = valid_ip_check(ip_address)

    if res['type'] is None:
        geo_json = valid_ip_check('check')
   
        response = [geo_json['latitude'], geo_json['longitude']]
    else:
        response = [res['latitude'], res['longitude']]
    return response


def get_location_details(coordinates):
    lat = coordinates[0]
    lng = coordinates[1]
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={google_map_api_key}"
    location_details_req = requests.get(url)
    req_json = json.loads(location_details_req.text)
    address_components = req_json['results'][0]
    street_name = address_components['address_components'][1]['long_name']
    return street_name


def valid_ip_check(param):
    send_url = f"http://api.ipstack.com/{param}?access_key={ip_stack_api_key}"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return geo_json


if __name__ == "__main__":
    # print("Host IP Address: ", get_host_name())
    print("The latitude and longitude details are:" , get_coordinates(ip_address))
    # print(get_coordinates())
    print("The location of the device is at:" ,get_location_details(get_coordinates(ip_address)))
    # print(get_location_details(get_coordinates(get_host_ip())))
