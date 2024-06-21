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
    (42.3601, -71.0589),  # Washington, DC
    (41.8781, -93.0977),  # Des Moines, IA
    # other cities
    
    
]
