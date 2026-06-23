def num_of_islands(grid):

    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(r, c):

        # boundary check, visited
        if(
            r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            grid[r][c] == 0 or
            (r, c)  in visited
        ):
            return
        
        visited.add((r, c))

        # explore neighbours
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    island = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                island += 1
                dfs(r, c)
            
    return island

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

print("no of islands found: ", num_of_islands(grid))

    
