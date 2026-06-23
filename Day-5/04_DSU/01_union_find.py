class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):

        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        
        # based on rank
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        
        else:
            self.parent[py] = px
            self.rank[px] += 1
        