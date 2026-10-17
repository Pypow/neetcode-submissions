# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node, count):
            if not node:
                return 0
            left, right = dfs(node.left, count), dfs(node.right, count)
            count += 1 + max(left, right)
            res[0] = max(res[0], 1 + left + right)
            return count
        dfs(root, 0)
        return res[0] - 1