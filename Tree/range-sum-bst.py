# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        level = [root]
        while level:
            node = level.pop()
            if node:
                if L <= node.val <= R:
                    total += node.val
                if L < node.val:
                    level.append(node.left)
                if node.val < R:
                    level.append(node.right)
        return total
