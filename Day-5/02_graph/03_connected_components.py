from collections import defaultdict

def count_connected_componets(n, edges):

    # create adjacency list
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

    count = 0

    for node in range(n):
        if node not in visited:
            count += 1
            dfs(node)
        
    return count

n = 5

edges = [
    [0, 1],
    [1, 2],
    [3, 4]
]

print(count_connected_componets(n, edges))
        
