from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()                   # Initiate Visited with empty Set
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            print("->", end=' ')
            dfs(graph, neighbor, visited)    # Recursivly call the same function

def bfs(graph, start):
    visited = set()                # Initiate Visited with empty Set
    queue = deque([start])         # Initialise Queue with start
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()           # Pop the first element
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
        print("\nQueue:", queue)

print("\n")
print("DFS traversal:")
dfs(graph, 'A')

print("\n")

print("BFS traversal:")
bfs(graph, 'A')





#....time complexity = O(V + E)
#....space complexity = O(V)