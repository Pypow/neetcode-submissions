# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0     # global_max
        def dfs(node, count):
            if not node:
                return 0
            count += 1
            nonlocal res
            res = max(res, count)
            left = dfs(node.left, count)
            right = dfs(node.right, count)
            return max(left, right)
        dfs(root, 0)
        return res