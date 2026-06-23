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

def post_order1(node):

    if not node:
        return ''
    
    post_order1(node.left)
    post_order1(node.right)
    print(node.val, end=' ')

def max_depth(node):

    if not node:
        return 0

    left_depth = max_depth(node.left)   
    right_depth = max_depth(node.right) 

    return 1 + max(left_depth, right_depth)  

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

root.post_order()
print()
post_order1(root)
print()
print(max_depth(root))