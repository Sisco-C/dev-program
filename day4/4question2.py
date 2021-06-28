import haversine as hs
Nairobi = (0.0236,37.9062)
Cairo =  (30.0444,31.2357)
# output distance in miles
hs.haversine(Nairobi, Cairo,)
from geopy.distance import geodesic
Cairo = (30.0444, 31.2357)
Nairobi = (1.2921, 36.8219)
print(geodesic(Cairo,Nairobi).miles,"miles")
