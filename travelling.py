import math

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_optimal_route(capitals):
    # find route
    route = [capitals[0]]
    remaining_capitals = capitals[1:]
    
    while remaining_capitals:
        current_city = route[-1]
        nearest_city = min(remaining_capitals, key = lambda city: distance(current_city, city))
        route.append(nearest_city)
        remaining_capitals.remove(nearest_city)
    return route
# Coordinates of cities
capitals = [
    (),  # Washington, DC
    (41.590833, -93.620833)  # Des Moines, IA
    
    (32.3675, -86.3), #Montgomery, Alabama
    (58.3, -134.416111) #Juneau, Alaska
    (33.448333, -112.073889) # Phoenix, Arizona
    (34.736111, -92.331111) #Little Rock, Arkansas
    (38.581667, -121.494444) #Sacramento, California
    (39.7392, -104.9849) # Denver, Colorado
    (41.7625, -72.674167) # Hartford, Connecticut
    (39.158056, -75.524444) # Dover, Delaware
    (30.438333, -84.280556) # Tallahassee, Florida
    (33.748889, -84.39)# Atlanta, Georgia
    (21.306944, -157.858333) # Honolulu,Hawaii
    (43.615833, -116.201667) #Boise County, Idaho
    (39.798333, -89.675833) #Springfield, Illinois
    (39.768611, -86.158056) #Indianapolis,  Indiana
    (39.034722, -95.695556) #Topeka, Kansas
    (38.2, -84.866667) # Frankfort, Kentucky
    
]

optimal_route = find_optimal_route(capitals)

for i, city in enumerate(optimal_route):
    print("Step {i+1}: {city}")
