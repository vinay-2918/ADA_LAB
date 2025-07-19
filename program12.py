from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]
start = int(input("Enter starting vertex: "))
print("BFS Traversal:", end=' ')
bfs(graph, start)
# This code implements the Breadth-First Search (BFS) algorithm for traversing a graph.
# The function bfs takes an adjacency matrix representation of the graph and a starting vertex.