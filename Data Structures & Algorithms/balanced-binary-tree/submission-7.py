# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                return [True, 0]
            left, right = dfs(node.left, height), dfs(node.right, height)
            isBal = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            height = 1 + max(left[1], right[1])     # imp: don't forget to update height
            return [isBal, height]
        return dfs(root, 0)[0]
    