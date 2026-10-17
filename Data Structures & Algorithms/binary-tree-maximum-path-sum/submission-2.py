# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = 0 if left < 0 else left
            right = 0 if right < 0 else right

            # with split
            maxSum = max(maxSum, left + right + node.val)
            
            # without split
            return max(left + node.val, right + node.val)
        dfs(root)
        return maxSum
