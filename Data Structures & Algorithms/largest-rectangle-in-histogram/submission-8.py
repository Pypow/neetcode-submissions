class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # only increasing heights are allowed in the stack
        # extend towards right using while loop check
        # extend towards left using start idx 
        stack = []      # [height, idx]
        res = 0
        for i in range(len(heights)):
            startIdx = i
            while stack and stack[-1][0] > heights[i]:
                h, idx = stack.pop()
                area = h * (i - idx)
                res = max(res, area)
                startIdx = idx
            stack.append([heights[i], startIdx])
        
        while stack:
            h, idx = stack.pop()
            area = h * (len(heights) - idx)     #IMP: NOT len(heights) - 1
            res = max(res, area)
        return res
        
