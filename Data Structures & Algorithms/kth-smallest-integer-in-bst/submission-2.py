# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def preOrder(node, res):
            if not node:
                return None
            
            preOrder(node.left, res)
            res.append(node.val)
            preOrder(node.right, res)
            return res
        res = preOrder(root, res)
        return res[k-1]
