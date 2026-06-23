from collections import deque

def graph_bfs(graph, start):

    queue = deque([start])
    visited = set([start])
    result = []

    while queue:

        level = []
        size = len(queue)

        for _ in range(size):

            node = queue.popleft()
            level.append(node)

            for neighbour in graph[node]:

                if neighbour not in visited:

                    visited.add(neighbour)
                    queue.append(neighbour)
        
        result.append(level)
            
    return result

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(graph_bfs(graph, "A"))