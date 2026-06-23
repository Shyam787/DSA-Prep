import heapq

def dijkstra(n, edges, src):

    graph = { i : [] for i in range(n)}

    for u, v, w, in edges:
        graph[u].append((v, w))

    dist = [float('inf')] * n
    dist[src] = 0

    heap = [(0, src)] # (dist, node)

    while heap:

        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        for neighbour, weight in graph[node]:

            new_dist = curr_dist + weight

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist

                heapq.heappush(heap, (new_dist, neighbour))

    return dist


# Test Case 1: Basic graph
n1 = 5
edges1 = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
src1 = 0

print("Test 1:", dijkstra(n1, edges1, src1))
# Expected: [0, 2, 3, 9, 6]


# Test Case 2: Single path chain
n2 = 4
edges2 = [
    (0, 1, 5),
    (1, 2, 3),
    (2, 3, 1)
]
src2 = 0

print("Test 2:", dijkstra(n2, edges2, src2))
# Expected: [0, 5, 8, 9]


# Test Case 3: Multiple paths to same node
n3 = 4
edges3 = [
    (0, 1, 10),
    (0, 2, 3),
    (2, 1, 1),
    (1, 3, 2),
    (2, 3, 8)
]
src3 = 0

print("Test 3:", dijkstra(n3, edges3, src3))
# Expected: [0, 4, 3, 6]


# Test Case 4: Disconnected graph
n4 = 5
edges4 = [
    (0, 1, 2),
    (1, 2, 3),
    (3, 4, 1)
]
src4 = 0

print("Test 4:", dijkstra(n4, edges4, src4))
# Expected: [0, 2, 5, inf, inf]


# Test Case 5: Source in middle
n5 = 6
edges5 = [
    (0, 1, 1),
    (1, 2, 2),
    (2, 3, 3),
    (4, 5, 1)
]
src5 = 2

print("Test 5:", dijkstra(n5, edges5, src5))
# Expected: [inf, inf, 0, 3, inf, inf]