from collections import defaultdict, deque

def topo_sort(n, edges):

    graph = defaultdict(list)
    indegree = [0] * n

    # building adjacency list
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()

    # adding node with 0 dependency
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    order = []

    while q:

        node = q.popleft()
        order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                q.append(neighbour)

    if len(order) != n:
        return "Cycle detected (Topological sort not possible)"
    
    return order


# Test Case 1
n1 = 4
edges1 = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 3]
]
print("Test 1:", topo_sort(n1, edges1))
# Expected: [0, 1, 2, 3] OR [0, 2, 1, 3]


# Test Case 2 (simple chain)
n2 = 3
edges2 = [
    [0, 1],
    [1, 2]
]
print("Test 2:", topo_sort(n2, edges2))
# Expected: [0, 1, 2]


# Test Case 3 (multiple valid orders)
n3 = 6
edges3 = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]
print("Test 3:", topo_sort(n3, edges3))
# Expected: valid topo order like [4, 5, 2, 3, 1, 0]


# Test Case 4 (cycle case)
n4 = 3
edges4 = [
    [0, 1],
    [1, 2],
    [2, 0]
]
print("Test 4:", topo_sort(n4, edges4))
# Expected: Cycle detected