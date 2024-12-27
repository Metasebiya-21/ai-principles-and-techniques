from collections import deque

def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Finds a path to traverse all cities starting from a given city.
    
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    if strategy not in ('bfs', 'dfs'):
        raise ValueError("Strategy must be 'bfs' or 'dfs'.")
    
    visited = set()
    path = []
    cost = 0

    def dfs(current_city):
        nonlocal cost
        visited.add(current_city)
        path.append(current_city)
        
        for neighbor, distance in roads[current_city]:
            if neighbor not in visited:
                cost += distance
                dfs(neighbor)
        
    def bfs():
        nonlocal cost
        queue = deque([(start_city, 0)]) 
        visited.add(start_city)
        
        while queue:
            current_city, current_cost = queue.popleft()
            path.append(current_city)
            cost = current_cost
            
            for neighbor, distance in roads[current_city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cost + distance))

    if strategy == 'dfs':
        dfs(start_city)
    elif strategy == 'bfs':
        bfs()

    return path, cost



if __name__ == '__main__':

    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    # Traverse all cities using BFS
    path_bfs, cost_bfs = traverse_all_cities(cities, roads, 'Addis Ababa', 'bfs')
    print("BFS Path:", path_bfs, "with cost:", cost_bfs)

    # Traverse all cities using DFS
    path_dfs, cost_dfs = traverse_all_cities(cities, roads, 'Addis Ababa', 'dfs')
    print("DFS Path:", path_dfs, "with cost:", cost_dfs)
