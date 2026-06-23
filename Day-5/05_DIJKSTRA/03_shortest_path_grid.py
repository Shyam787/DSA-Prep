import heapq

def shortest_path(grid):

    n = len(grid)
    m = len(grid[0])

    dist = [ [float('inf')] * m for _ in range(n) ]
    dist[0][0] = grid[0][0]

    heap = [(dist[0][0], 0, 0)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while heap:

        cost, r, c = heapq.heappop(heap)

        if cost > dist[r][c]:
            continue
            
        if r == n - 1 and c == m - 1:
            return cost
        
        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m:

                new_cost = cost + grid[nr][nc]

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost

                    heapq.heappush(heap, (new_cost, nr, nc))

    return -1

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(shortest_path(grid))
# Expected output: 7