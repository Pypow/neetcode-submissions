# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
        
            lheight, lbalance = dfs(node.left)
            rheight, rbalance = dfs(node.right)
            
            height = 1 + max(lheight, rheight)

            if not(lbalance and rbalance):
                return [height, False]
            balance = abs(lheight - rheight) <= 1
            return [height, balance]
        h, res = dfs(root)
        return res
