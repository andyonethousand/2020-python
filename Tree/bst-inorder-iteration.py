# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current != None or stack:                
            while current != None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result
        
