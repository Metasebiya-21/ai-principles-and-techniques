import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def visualize_graph(roads, path=None):
    """
    Visualizes the graph of cities and roads.
    Highlights the path if provided.
    """
    G = nx.Graph()
    
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title("Graph Visualization")
    plt.show()


def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Implements BFS and DFS to find paths in the city graph.
    """
    if strategy not in ('bfs', 'dfs'):
        raise ValueError("Strategy must be 'bfs' or 'dfs'.")
    
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


def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Implements traversal of all cities starting from start_city.
    """
    visited = set()
    path = []
    total_cost = 0

    def dfs(city):
        nonlocal total_cost
        visited.add(city)
        path.append(city)
        
        for neighbor, distance in roads[city]:
            if neighbor not in visited:
                total_cost += distance
                if dfs(neighbor):
                    return True
                total_cost -= distance
        
        if len(visited) == len(cities):
            return True
        
        visited.remove(city)
        path.pop()
        return False

    if strategy == 'dfs':
        dfs(start_city)
    elif strategy == 'bfs':
        raise NotImplementedError("BFS traversal for all cities is not implemented.")
    
    return path, total_cost

if __name__ == '__main__':

    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    visualize_graph(cities, roads)

    # Find a path from Addis Ababa to Mekelle using BFS
    path, cost = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'bfs')
    print("BFS Path:", path, "with cost:", cost)

    # Find a path from Addis Ababa to Mekelle using DFS
    path, cost = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'dfs')
    print("DFS Path:", path, "with cost:", cost)

    # Traverse all cities starting from Addis Ababa
    path, cost = traverse_all_cities(cities, roads, 'Addis Ababa', 'dfs')
    print("Traversal Path:", path, "with total cost:", cost)
