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

def delete(node, del_val):

    if not node:
        return None
    
    if del_val < node.val:
        node.left = delete(node.left, del_val)

    elif del_val > node.val:
        node.right = delete(node.right, del_val)

    else:

        # case 1 + case 2
        if not node.left:
            return node.right
        
        if not node.right:
            return node.left
        
        # case 3

        sucessor = node.right
         
        while sucessor.left:
            sucessor = sucessor.left
        
        node.val = sucessor.val

        node.right = delete(node.right, sucessor.val)

    return node

root1 = Node(5)

root1.left = Node(3)
root1.right = Node(7)

root1.left.left = Node(2)
root1.left.right = Node(4)

root1.right.left = Node(6)
root1.right.right = Node(10)

root1.right.right.right = Node(12)

root1.in_order()
print()

# case1 - one child
delete(root1, 10)
root1.in_order()
print()

# case2 - leaf node
delete(root1, 12)
root1.in_order()
print()

# case3 - 2 child
delete(root1, 3)
root1.in_order()
print()
