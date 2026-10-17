# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ldepth = 0
        rdepth = 0
        def dfs(node):
            if not node:
                return 0
            ldepth = 1 + dfs(node.left)
            rdepth = 1 + dfs(node.right)
            return max(ldepth, rdepth)
        return dfs(root)


            
            