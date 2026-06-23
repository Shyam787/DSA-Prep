def kruskal(n, edges):

    # sort edges by weight
    edges.sort(key = lambda x: x[2])

    # DSU
    parent = list(range(n))
    rank = [0] * n

    def find(x):

        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]
    
    def union(x, y):

        px, py = find(x), find(y)

        if px == py:
            return False
        
        if rank[px] > rank[py]:
            parent[py] = px
        
        elif rank[py] > rank[px]:
            parent[px] = py
        
        else:
            parent[py] = px
            rank[px] += 1

        return True

    # MST
    cost = 0
    count = 0

    for u, v, w in edges:
        if union(u, v):
            cost += w
            count += 1
        
        if count == n-1:
            break
    
    return cost

n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("MST Cost:", kruskal(n, edges))
        
