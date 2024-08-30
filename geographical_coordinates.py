
import math

def calculate_distance(coord1, coord2):
    R = 6371
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

def find_nearest_location(locations, current_location):
    nearest_locatoion = None
    min_distance = float('inf')
    for location in locations:
        distance = calculate_distance(current_location, location)
        if distance < min_distance:
            min_distance = distance
            nearest_locatoion = location
    return nearest_locatoion, min_distance

locations = [(40.7128, -74.0060), (41.8781, -87.6298), (34.0522, -118.2437)]
current_location = (37.7749, -122.4194)
nearest_location, distance = find_nearest_location(locations, current_location)
print(f"Nearest Location: {nearest_location}")
print(f"Distance: {distance:.2f} km")