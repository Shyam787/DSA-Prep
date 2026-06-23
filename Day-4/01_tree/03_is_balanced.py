class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(node):

    def dfs(node):
        if not node:
            return 0
        
        left_height = dfs(node.left)
        if left_height == -1:
            return -1
        
        right_height = dfs(node.right)
        if right_height == -1:
            return -1 
        
        if abs(right_height - left_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return dfs(node) != -1

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print("Balanced Tree: ", is_balanced(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
print("Balanced Tree: ", is_balanced(root2))