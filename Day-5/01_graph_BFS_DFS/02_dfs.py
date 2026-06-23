def graph_dfs_recursive(graph, node, visited, result):

    if not node:
        return []
    
    visited.add(node)
    result.append(node)

    for neighbour in graph[node]:

        if neighbour not in visited:
            
            graph_dfs_recursive(graph, neighbour, visited, result)

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = set()
result = []

graph_dfs_recursive(graph, "A", visited, result)
print("recursive approach: ", result)


# stack for deeper nodes and optimization

def graph_dfs_stack(graph, start):

    stack = [start]
    visited1 = set([start])
    result1 = []

    while stack:

        node = stack.pop()
        result1.append(node)

        for neighbour in graph[node]:

            if neighbour not in visited1:
                visited1.add(neighbour)
                stack.append(neighbour)
    
    return result1


print("stack approach", graph_dfs_stack(graph, "A"))
