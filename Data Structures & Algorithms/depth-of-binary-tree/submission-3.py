# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ---- DFS iterative -----
        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res

        # ---- DFS recursive ----
        # if not root:
        #     return 0

        # ldepth = self.maxDepth(root.left) + 1
        # rdepth = self.maxDepth(root.right) + 1
        # return max(ldepth, rdepth)


        # ---- BFS iterative ----
        q = deque()
        res = 0
        
        if root:
            q.append(root)

        while q:
            res += 1
            for n in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
                    
        


