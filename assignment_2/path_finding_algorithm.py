from collections import deque


def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Finds a path from start_city to goal_city using the specified strategy.
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps for unweighted, or distance for weighted graphs) of the path.
    """
    if strategy not in ('bfs', 'dfs'):
        raise ValueError("Strategy must be 'bfs' or 'dfs'.")

    if start_city not in cities or goal_city not in cities:
        raise ValueError("Start or goal city is not in the list of valid cities.")
    
    missing_cities = [city for city in cities if city not in roads]
    if missing_cities:
        raise ValueError(f"The following cities are not in the roads dictionary: {missing_cities}")
    
    frontier = deque([[start_city]]) if strategy == 'bfs' else [[start_city]]
    visited = set()
    
    while frontier:
        path = frontier.popleft() if strategy == 'bfs' else frontier.pop()
        current_city = path[-1]
    
        if current_city == goal_city:
            cost = 0
            for i in range(len(path) - 1):
                for neighbor, distance in roads[path[i]]:
                    if neighbor == path[i + 1]:
                        cost += distance
                        break
            return path, cost
    
        if current_city not in visited:
            visited.add(current_city)
            for neighbor, distance in roads[current_city]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    frontier.append(new_path)
    
    return None, 0 

if __name__ == '__main__':
    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    # Valid scenario
    path, cost = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'bfs')
    print("Path:", path, "Cost:", cost)

    # Invalid scenario (start city not in cities list)
    try:
        uninformed_path_finder(cities, roads, 'Invalid City', 'Mekelle', 'bfs')
    except ValueError as e:
        print(e)
