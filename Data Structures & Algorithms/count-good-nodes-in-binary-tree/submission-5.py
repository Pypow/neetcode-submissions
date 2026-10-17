# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prevMax):
            if not node:
                return 0
            good = 0
            if node.val >= prevMax:
                prevMax = max(prevMax, node.val)
                good = 1
            
            total = good + dfs(node.left, prevMax) + dfs(node.right, prevMax)
            return total
        
        return dfs(root, float("-inf"))
            
            