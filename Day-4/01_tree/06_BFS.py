from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_bfs(root):

    queue = deque([root])
    result = []

    if not root:
        return []
    
    while queue:

        level = []
        size = len(queue)

        for _ in range(size):

            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print(tree_bfs(root))