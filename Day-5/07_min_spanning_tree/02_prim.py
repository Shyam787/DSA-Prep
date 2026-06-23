import heapq

def prim(n, edges):

    graph = { i : [] for i in range(n)}

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = set()
    heap = [(0, 0)]

    total_cost = 0

    while len(visited) < n:

        cost, node = heapq.heappop(heap)

        if node in visited:
            continue
        
        visited.add(node)
        total_cost += cost

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(heap, (weight, neighbour))

    return total_cost


n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("MST Cost using Prim:", prim(n, edges))