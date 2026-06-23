def bellman_ford(n, edges, src):

    dist = [float('inf')] * n
    dist[src] = 0

    # Step 1: Relax edges V-1 times

    for _ in range(n-1):

        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 2: Detect negative cycle

    for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return  "Negative Cycle Exists"
            
    return dist



# ---------------------------
# TEST CASE 1: Normal Graph
# ---------------------------
n1 = 5
edges1 = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]

print("Test 1 Output:", bellman_ford(n1, edges1, 0))


# ---------------------------
# TEST CASE 2: Negative Cycle
# ---------------------------
n2 = 3
edges2 = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 0, -1)  # negative cycle
]

print("Test 2 Output:", bellman_ford(n2, edges2, 0))