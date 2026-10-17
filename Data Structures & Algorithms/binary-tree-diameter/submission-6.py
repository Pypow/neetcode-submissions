# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0     # global diameter
        def dfs(node, count):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left, count)
            right = dfs(node.right, count)
            res = max(res, left + right)     # consider current node
            return 1 + max(left, right)
        dfs(root, 0)
        return res

