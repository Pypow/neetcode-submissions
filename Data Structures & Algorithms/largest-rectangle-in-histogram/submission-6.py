class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # h, idx
        res = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                h, idx = stack.pop()
                start = idx
                area = h * (i - idx)
                res = max(res, area)
            stack.append((heights[i], start))

        while stack:
            h, idx = stack.pop()
            area = h * (len(heights) - idx)
            res = max(res, area)
        return res

        
        
