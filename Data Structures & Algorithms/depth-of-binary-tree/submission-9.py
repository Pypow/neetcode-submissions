# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, count):
            if not node:
                return 0
            count += 1 + max(dfs(node.left, count), dfs(node.right, count))
            return count
        return dfs(root, 0)


            
