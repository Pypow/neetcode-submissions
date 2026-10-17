# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # all vals to left of root must be less than root
        # all vals to right of root must be greater than root
        # this condition must be true for any given node
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            left = dfs(node.left, left, node.val)
            right = dfs(node.right, node.val, right)
            return left and right
        return dfs(root, float("-inf"), float("inf"))