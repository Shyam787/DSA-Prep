class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def in_order(self):
        
        if self.left:
            self.left.in_order()
        print(self.val, end=' -> ')
        if self.right:
            self.right.in_order()

def insertion(node, val):

    if not node:
        return Node(val)
    
    if node.val > val:
        node.left = insertion(node.left, val)
    
    else:
        node.right = insertion(node.right, val)

    return node

root1 = Node(5)

root1.left = Node(3)
root1.right = Node(7)

root1.left.left = Node(2)
root1.left.right = Node(4)

root1.right.left = Node(6)
root1.right.right = Node(10)

root1.in_order()
print()

insertion(root1, 8)
root1.in_order()


