

import math

# (latitude, longitude)
state_capitals = {
    'Iowa': (41.5908, -93.6208),
    'Washington DC': (38.89511, -77.03637),
    'Alabama': (32.377716, -86.300568),
    'Alaska': (58.301598, -134.420212),
    'Arizona': (33.448143, -112.096962),
    'Arkansas': (34.746613, -92.288986),
    'California': (38.576668, -121.493629),
    'Colorado': (39.739227, -104.99025),
    'Connecticut': (41.764046, -72.682167),
    'Delaware': (39.157307, -75.519722),
    'Florida': (30.438118, -84.281296),
    'Georgia': (33.749027, -84.388229),
    'Hawaii': (21.307442, -157.857376),
    'Idaho': (43.617775, -116.199722),
    'Illinois': (39.798363, -89.654961),
    'Indiana': (39.768623, -86.162643),
    'Kansas': (39.048191, -95.677956),
    'Kentucky': (38.186722, -84.875374),
    'Louisiana': (30.457069, -91.187393),
    'Maine': (44.307167, -69.781693),
    'Maryland': (38.978764, -76.490936),
    'Massachusetts': (42.358162, -71.063698),
    'Michigan': (42.733635, -84.555328),
    'Minnesota': (44.955097, -93.102211),
    'Mississippi': (32.303848, -90.182106),
    'Missouri': (38.579201, -92.172935),
    'Montana': (46.585709, -112.018417),
    'Nebraska': (40.808075, -96.699654),
    'Nevada': (39.163914, -119.766121),
    'New Hampshire': (43.206898, -71.537994),
    'New Jersey': (40.220596, -74.769913),
    'New Mexico': (35.68224, -105.939728),
    'New York': (42.652843, -73.757874),
    'North Carolina': (35.78043, -78.639099),
    'North Dakota': (46.82085, -100.783318),
    'Ohio': (39.961346, -82.999069),
    'Oklahoma': (35.492207, -97.503342),
    'Oregon': (44.938461, -123.030403),
    'Pennsylvania': (40.264378, -76.883598),
    'Rhode Island': (41.830914, -71.414963),
    'South Carolina': (34.000343, -81.033211),
    'South Dakota': (44.367031, -100.346405),
    'Tennessee': (36.16581, -86.784241),
    'Texas': (30.27467, -97.740349),
    'Utah': (40.777477, -111.888237),
    'Vermont': (44.262436, -72.580536),
    'Virginia': (37.538857, -77.43364),
    'Washington': (47.037874, -122.900695),
    'West Virginia': (38.336246, -81.612328),
    'Wisconsin': (43.074684, -89.384445),
    'Wyoming': (41.140259, -104.820236)
}

# Calculate the distance between two points using the Haversine formula
def haversine(coord1, coord2):
    R = 6371  # Earth radius in kilometers
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Create a distance matrix
distances = {}
for cap1 in state_capitals:
    distances[cap1] = {}
    for cap2 in state_capitals:
        if cap1 != cap2:
            distances[cap1][cap2] = haversine(state_capitals[cap1], state_capitals[cap2])

def nearest_city(distances, start, end):
    unvisited = set(state_capitals.keys())
    unvisited.remove(start)
    path = [start]
    current = start
    total_distance = 0

    while unvisited:
        nearest = min(unvisited, key=lambda city: distances[current][city])
        total_distance += distances[current][nearest]
        current = nearest
        path.append(current)
        unvisited.remove(current)
    total_distance += distances[current][end]
    path.append(end)
    return path, total_distance

start = 'Iowa'
end = 'Washington DC'
route, length = nearest_city(distances, start, end)

print("Most efficient route:", route)
print("Total distance (km):", length)
