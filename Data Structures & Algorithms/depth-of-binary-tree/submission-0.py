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
        if not root:
            return 0
        
        ldepth = self.maxDepth(root.left) + 1
        rdepth = self.maxDepth(root.right) + 1
        return max(ldepth, rdepth)