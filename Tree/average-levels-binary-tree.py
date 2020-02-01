# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [root.val]

        level = [root]
        result = []

        while level:
            queue = []
            for node in level:
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            result.append(sum([n.val for n in level]) / len(level))
            level = queue

        return result
