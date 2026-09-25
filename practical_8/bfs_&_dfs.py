# Practical 8
# Implementation of Graph and Searching (DFS and BFS)

from collections import deque


# Graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# DFS - Depth First Search
def dfs(graph, start, visited=None):

    if visited is None:
        visited = set()

    # Mark current node as visited
    visited.add(start)

    print(start, end=" ")

    # Visit all adjacent nodes
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# BFS - Breadth First Search
def bfs(graph, start):

    visited = set()
    queue = deque([start])

    # Mark starting node as visited
    visited.add(start)

    while queue:

        # Remove the first node from queue
        node = queue.popleft()

        print(node, end=" ")

        # Add unvisited adjacent nodes
        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Main program
print("GRAPH TRAVERSAL USING DFS AND BFS")
print("-" * 40)

print("\nGraph:")
for node in graph:
    print(node, "->", graph[node])

print("\nDFS Traversal:")
dfs(graph, 'A')

print("\n\nBFS Traversal:")
bfs(graph, 'A')

print()