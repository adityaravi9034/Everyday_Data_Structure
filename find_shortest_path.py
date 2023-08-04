"""Given a weighted directed graph represented as an adjacency list, write a function to find the shortest path between two nodes, A and B.
The weight of each edge is a positive integer, and there are no negative cycles in the graph.

Function Signature: def find_shortest_path(graph: dict, A: str, B: str) -> List[str]:

Input:

graph: A dictionary representing the adjacency list of the graph. The keys are strings representing the nodes, 
      and the values are lists of tuples (neighbor_node, weight) representing the neighboring nodes and their corresponding edge weights.
A: The starting node from which to find the shortest path.
B: The destination node to which to find the shortest path.
Output:

Return a list of nodes representing the shortest path from node A to node B. If there is no path from A to B, return an empty list.
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 2)],
    'D': [('E', 1)],
    'E': [('B', 3)],
}

find_shortest_path(graph, 'A', 'D')  # Output: ['A', 'C', 'D']
find_shortest_path(graph, 'B', 'E')  # Output: ['B', 'D', 'E']
find_shortest_path(graph, 'A', 'F')  # Output: []
"""

from heapq import heappush, heappop

def find_shortest_path(graph, A, B):
    # Initialize distances and predecessors dictionaries
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}

    # Priority queue to store nodes with their current distance from A
    priority_queue = [(0, A)]
    distances[A] = 0

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)

        if current_node == B:
            # Reconstruct the path from A to B using predecessors
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heappush(priority_queue, (distance, neighbor))

    # If there is no path from A to B, return an empty list
    return []

# Example graph
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 2)],
    'D': [('E', 1)],
    'E': [('B', 3)],
}

print(find_shortest_path(graph, 'A', 'D'))  # Output: ['A', 'C', 'D']
print(find_shortest_path(graph, 'B', 'E'))  # Output: ['B', 'D', 'E']
print(find_shortest_path(graph, 'A', 'F'))  # Output: []
