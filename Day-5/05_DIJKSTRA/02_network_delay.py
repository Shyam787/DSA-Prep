import heapq
from collections import defaultdict

def network_delay_time(times, n, k):

    graph = defaultdict(list)
    
    for u, v, w in times:
        graph[u].append((v, w))

    dist = { i : float('inf') for i in range(1, n + 1)}
    dist[k] = 0

    heap = [(0, k)]

    while heap:

        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        for neighbour, weight in graph[node]:

            new_dist = curr_dist + weight

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist

                heapq.heappush(heap, (new_dist, neighbour))

    max_time = max(dist.values())

    return -1 if max_time == float('inf') else max_time

times = [
    (2, 1, 1),
    (2, 3, 1),
    (3, 4, 1)
]

n = 4
k = 2

print(network_delay_time(times, n, k))
# Expected output: 2