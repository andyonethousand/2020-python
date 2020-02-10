# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, result):
            if root != None:
                if root.left != None:
                    helper(root.left, result)

                result.append(root.val)

                if root.right != None:
                    helper(root.right, result)

        result = []
        helper(root, result)
        return result


        
