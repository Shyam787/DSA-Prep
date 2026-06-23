class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(node, p, q):

    if not node:
        return None
    
    if node.val == p or node.val == q:
        return node
    
    left = lowest_common_ancestor(node.left, p, q)
    right = lowest_common_ancestor(node.right, p, q)

    if left and right:
        return node
    
    return left if left else right


root = Node(3)

root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)

root.right.left = Node(0)
root.right.right = Node(8)

ancestor = lowest_common_ancestor(root, 6, 8)

print("Lowest Common Ancestor:", ancestor.val)