class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def post_order(self):
        
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val, end=' ')

def invert_tree(node):

    if not node:
        return 0
    
    node.left, node.right = node.right, node.left

    invert_tree(node.left)
    invert_tree(node.right)

    return node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.post_order()

invert_tree(root)

root.post_order()
