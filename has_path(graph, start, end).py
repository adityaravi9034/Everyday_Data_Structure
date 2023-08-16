"""
You are given an undirected graph represented as an adjacency list and two nodes, start and end. Your task is to determine if there exists
a path between the start and end nodes.

Write a function has_path(graph, start, end) that takes the adjacency list of the graph, and the start and end nodes as inputs, and returns 
True if a path exists between the two nodes,
and False otherwise.

The graph is represented as a dictionary, where the keys are the nodes and the values are lists of neighboring nodes.

Example:

graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: [5],
    5: []
}
start = 0
end = 5

result = has_path(graph, start, end)
print(result)  # Output: True

Explanation: In this example, there exists a path from node 0 to node 5: 0 -> 2 -> 4 -> 5.
"""

def has_path(graph, start, end):
    visited = set()

    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)

# Example usage:
graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: [5],
    5: []
}
start = 0
end = 5

result = has_path(graph, start, end)
print(result)  # Output: True
