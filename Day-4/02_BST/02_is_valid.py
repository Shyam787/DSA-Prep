class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isvalid_BST(node):

    def dfs(node, low, high):
        if not node:
            return True
        
        if not (low < node.val < high):
            return False
        
        return (
            dfs(node.left, low, node.val) and
            dfs(node.right, node.val, high)
        )
        

    return dfs(node, float('-inf'), float('inf'))

root1 = Node(5)

root1.left = Node(3)
root1.right = Node(7)

root1.left.left = Node(2)
root1.left.right = Node(4)

root1.right.left = Node(6)
root1.right.right = Node(10)
        
print(isvalid_BST(root1))