def flood_fill(image, sr, sc, color):

    rows = len(image)
    cols = len(image[0])

    original = image[sr][sc]

    # imp check 
    if original == color:
        return image

    def dfs(r, c):

        if (
            r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            image[r][c] != original
        ):
            return
        
        image[r][c] = color

        # connected neighbours
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)

    return image

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

sr = 0
sc = 0
color = 2

result = flood_fill(image, sr, sc, color)

print("Flood Filled Image:")
for row in result:
    print(row)
        
        
