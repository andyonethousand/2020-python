# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BST
# 1) Recursion, linear time and space
# 2) Iteration, linear time and space
# 3) Inorder, linear time and space
# Why use DFS instead of BFS?

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if node == None:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False

            if helper(node.right, val, upper) == False:
                return False

            if helper(node.left, lower, val) == False:
                return False

            return True

        return helper(root)
