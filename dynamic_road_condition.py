from assignment_2.path_finding_algorithm import uninformed_path_finder
def handle_blocked_roads(roads, blocked_roads):
    """
    Modifies the roads dictionary to handle blocked roads.

    Parameters:
    - roads: Original dictionary of city connections.
    - blocked_roads: List of blocked roads as tuples (city1, city2).

    Returns:
    - updated_roads: Updated dictionary with blocked roads removed.
    """
    updated_roads = {city: list(connections) for city, connections in roads.items()}
    
    for city1, city2 in blocked_roads:
        updated_roads[city1] = [(c, d) for c, d in updated_roads[city1] if c != city2]
        updated_roads[city2] = [(c, d) for c, d in updated_roads[city2] if c != city1]
    
    return updated_roads

if __name__ == '__main__':
    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']

    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }
    blocked_roads = [('Addis Ababa', 'Bahir Dar')]
    updated_roads = handle_blocked_roads(roads, blocked_roads)
    path, cost = uninformed_path_finder(cities, updated_roads, 'Addis Ababa', 'Mekelle', 'bfs')
    print("Path:", path, "Cost:", cost)

