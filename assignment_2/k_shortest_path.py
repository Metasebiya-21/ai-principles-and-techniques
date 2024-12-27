import heapq

def k_shortest_paths(cities, roads, start_city, goal_city, k):
    """
    Finds the k-shortest paths between two cities.

    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The starting city.
    - goal_city: The destination city.
    - k: The number of shortest paths to find.

    Returns:
    - paths: List of tuples (path, cost) for the k-shortest paths.
    """

    if start_city not in cities or goal_city not in cities:
        raise ValueError(f"Start city or goal city not in cities list.")

    queue = [(0, [start_city])]
    all_paths = []

    while queue and len(all_paths) < k:
        cost, path = heapq.heappop(queue)
        current_city = path[-1]

        if current_city == goal_city:
            all_paths.append((path, cost))
            continue

        for neighbor, distance in roads[current_city]:
            if neighbor in cities and neighbor not in path:
                new_path = path + [neighbor]
                heapq.heappush(queue, (cost + distance, new_path))

    return all_paths
if __name__ == '__main__':
    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    shortest_paths = k_shortest_paths(cities, roads, 'Addis Ababa', 'Mekelle', 2)
    for i, (path, cost) in enumerate(shortest_paths):
        print(f"Path {i+1}: {path} with cost: {cost}")
