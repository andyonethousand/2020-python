# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            # get last item of stack
            root, lower, upper = stack.pop()

            if root == None:
                continue

            val = root.val
            if val <= lower or val >= upper:
                return False

            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))

        return True
    
