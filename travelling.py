import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from geopy.distance import geodesic

# Set a fixed random seed for reproducibility
np.random.seed(42)

# Read the CSV file
filename = 'C:/Users/18378/OneDrive/桌面/tpp/us-state-capitals.csv'
data = pd.read_csv(filename)

# Extract coordinates and city names
coordinates = data[['latitude', 'longitude']].values #coordinates of capital cities
cities = data['origin'].values # file's column title, means the capital names


# Define start and end cities
start_city = 'Iowa' # set starting city
end_city = 'Washington D.C.' # set end city

# Determine the indices for start and end cities
try:
    start_idx = list(cities).index(start_city) #Finds the index of the start city (Iowa) in the cities array.
    end_idx = list(cities).index(end_city) #Finds the index of the end city (Washington D.C.) in the cities array.
except ValueError as e:
    print(f"Error: {e}")
    print("Available cities:", cities)
    exit()

# Clustering
num_clusters = 5  # Set the number of clusters; adjust as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(coordinates)
labels = kmeans.labels_

# Function to calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += geodesic(
            (coordinates[route[i]][0], coordinates[route[i]][1]),
            (coordinates[route[i + 1]][0], coordinates[route[i + 1]][1])
        ).km
    return total_distance

# 2-Opt Algorithm for local optimization within clusters
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if calculate_total_distance(new_route) < calculate_total_distance(best):
                    best = new_route
                    improved = True
        route = best
    return best

# Generate the route for each cluster with optimization
def generate_cluster_route(cluster_indices, start_city=None, end_city=None):
    if start_city is not None:
        cluster_indices = [start_city] + [i for i in cluster_indices if i != start_city]
    if end_city is not None:
        cluster_indices = [i for i in cluster_indices if i != end_city] + [end_city]
    
    optimized_route = two_opt(cluster_indices)
    return optimized_route

# Generate the route across all clusters
total_route = []

for cluster_id in range(num_clusters):
    cluster_indices = [i for i, x in enumerate(labels) if x == cluster_id]

    if cluster_id == 0:
        route = generate_cluster_route(cluster_indices, start_city=start_idx)
    elif cluster_id == num_clusters - 1:
        route = generate_cluster_route(cluster_indices, end_city=end_idx)
    else:
        route = generate_cluster_route(cluster_indices)

    total_route.extend(route)

# Remove duplicates and ensure the route starts with Iowa and ends with Washington
total_route = list(dict.fromkeys(total_route))
total_route = [i for i in total_route if i != start_idx and i != end_idx]
total_route = [start_idx] + total_route + [end_idx]

# Calculate the total distance in miles
total_distance_km = calculate_total_distance(total_route)
total_distance_miles = total_distance_km * 0.621371

# Output the final route and total distance
final_route = [cities[i] for i in total_route]
print("Complete route:", " -> ".join(final_route))
print("Total distance:", total_distance_miles, "miles")
