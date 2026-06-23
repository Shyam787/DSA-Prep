from collections import deque

def rotten_oranges(grid):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 2:
                queue.append((r, c))
            
            if grid[r][c] == 1:
                fresh += 1

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),  
    ]

    minutes = 0

    while queue and fresh > 0:

        size = len(queue)

        for _ in range(size):

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc
            
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2

                    fresh -= 1
                    queue.append((nr, nc))
        
        minutes += 1
    
    return minutes if fresh == 0 else -1

grid = [
 [2,1,1],
 [1,1,0],
 [0,1,1]
]

print(rotten_oranges(grid))
