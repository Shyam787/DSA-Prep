from collections import defaultdict, deque

def can_finish(n, prerequisites):

    graph = defaultdict(list)
    indegree = [0] * n

    # build graph
    for u, v in prerequisites:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    count = 0
    order = []

    while q:

        node = q.popleft()
        count += 1
        order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                q.append(neighbour)

    if count == n:
        return True, order
    else:
        return False, []

# Test Case 1: Possible (simple chain)
n1 = 2
prereq1 = [[1, 0]]

print("Test 1:", can_finish(n1, prereq1))
# Expected: True


# Test Case 2: Cycle exists
n2 = 2
prereq2 = [[1, 0], [0, 1]]

print("Test 2:", can_finish(n2, prereq2))
# Expected: False


# Test Case 3: Larger DAG
n3 = 4
prereq3 = [[1, 0], [2, 1], [3, 2]]

print("Test 3:", can_finish(n3, prereq3))
# Expected: True


# Test Case 4: Multiple independent chains
n4 = 5
prereq4 = [[1, 0], [2, 0], [3, 1], [4, 2]]

print("Test 4:", can_finish(n4, prereq4))
# Expected: True


# Test Case 5: Cycle in middle
n5 = 3
prereq5 = [[0, 1], [1, 2], [2, 0]]

print("Test 5:", can_finish(n5, prereq5))
# Expected: False