class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

diameter = 0

def max_diameter(node):

    global diameter

    if not node:
        return 0
    
    left_height = max_diameter(node.left)
    right_height = max_diameter(node.right)

    diameter = max(diameter, left_height + right_height)

    return 1 + max(left_height, right_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(4)

max_diameter(root)

print(diameter)