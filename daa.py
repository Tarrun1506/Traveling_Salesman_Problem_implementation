import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Get input from the user
def get_locations():
    num_locations = int(input("Enter the number of locations: "))
    locations = {}
    for i in range(num_locations):
        loc_name = f"Location {i + 1}"
        x, y = map(int, input(f"Enter coordinates (x y) for {loc_name}: ").split())
        locations[loc_name] = (x, y)
    return locations

# Create a distance matrix
def create_distance_matrix(locations):
    return {
        loc1: {
            loc2: calculate_distance(locations[loc1], locations[loc2]) for loc2 in locations
        }
        for loc1 in locations
    }

# Brute force TSP (for smaller datasets)
def tsp_brute_force(locations, distance_matrix):
    all_permutations = permutations(locations.keys())
    shortest_path = None
    min_distance = float('inf')
    
    for perm in all_permutations:
        distance = 0
        for i in range(len(perm) - 1):
            distance += distance_matrix[perm[i]][perm[i + 1]]
        distance += distance_matrix[perm[-1]][perm[0]]  # Return to start
        
        if distance < min_distance:
            min_distance = distance
            shortest_path = perm
    
    return shortest_path, min_distance

# Visualize the result
def visualize_shortest_path(locations, path, distance):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot locations
    for loc, coord in locations.items():
        ax.scatter(*coord, label=loc, s=100, zorder=5)
        ax.text(coord[0] + 1, coord[1] + 1, loc, fontsize=10)
    
    # Plot the path
    x_coords = [locations[loc][0] for loc in path] + [locations[path[0]][0]]
    y_coords = [locations[loc][1] for loc in path] + [locations[path[0]][1]]
    ax.plot(x_coords, y_coords, 'b-', zorder=4, label='Path')
    
    # Display the total distance
    ax.set_title(f"Shortest Path (Distance: {distance:.2f})")
    ax.legend()
    plt.grid()
    plt.show()

# Main Program
locations = get_locations()
distance_matrix = create_distance_matrix(locations)
shortest_path, min_distance = tsp_brute_force(locations, distance_matrix)
visualize_shortest_path(locations, shortest_path, min_distance)
