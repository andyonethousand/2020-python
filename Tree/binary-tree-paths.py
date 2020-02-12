# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        
        # Easy solution, but you're too tired I guess in Spain to figure out the logic
        while stack:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                paths.append(path)
            if node.left != None:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right != None:
                stack.append((node.right, path + '->' + str(node.right.val)))
            
        return paths
